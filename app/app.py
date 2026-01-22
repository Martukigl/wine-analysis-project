import joblib
import pandas as pd
from pathlib import Path
import streamlit as st

# -----------------------------
# Typical ranges (reference-only, NOT causal)
# -----------------------------
# Approximate "typical" ranges seen in the dataset (used to surface unusual inputs)
TYPICAL_RANGES = {
    "volatile acidity": (0.2, 0.7),
    "alcohol": (9.5, 12.5),
    "total sulfur dioxide": (20, 100),
    "chlorides": (0.03, 0.09),
    "density": (0.994, 0.999),
    "sulphates": (0.4, 0.8),
}

def detect_risk_flags(wine: dict) -> list:
    """Flag inputs that fall outside typical dataset ranges (interpretation aid only)."""
    flags = []
    for feature, (low, high) in TYPICAL_RANGES.items():
        value = wine.get(feature, None)
        if value is None:
            continue
        if value < low:
            flags.append(f"{feature}: unusually low ({value})")
        elif value > high:
            flags.append(f"{feature}: unusually high ({value})")
    return flags


# -----------------------------
# App config
# -----------------------------
st.set_page_config(
    page_title="Wine Quality Risk Calculator",
    page_icon="🍷",
    layout="centered"
)

st.title("🍷 Wine Quality Risk Calculator")
st.caption("Inference-only tool to flag low technical quality risk from chemical composition.")

# -----------------------------
# Load artifacts
# -----------------------------
MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "histgb_risk_model.joblib"
THRESH_PATH = Path(__file__).resolve().parents[1] / "models" / "risk_thresholds.joblib"

@st.cache_resource
def load_artifacts():
    model = joblib.load(MODEL_PATH)
    thresholds = joblib.load(THRESH_PATH)
    frozen_threshold = float(thresholds.get("histgb_frozen_threshold", 0.288))
    return model, frozen_threshold

try:
    model, FROZEN_THRESHOLD = load_artifacts()
except FileNotFoundError as e:
    st.error("Model artifacts not found. Please check your /models folder.")
    st.code(str(e))
    st.stop()

# -----------------------------
# Feature schema
# -----------------------------
FEATURES = [
    "fixed acidity",
    "volatile acidity",
    "citric acid",
    "residual sugar",
    "chlorides",
    "free sulfur dioxide",
    "total sulfur dioxide",
    "density",
    "pH",
    "sulphates",
    "alcohol",
]

def validate_and_build_df(x: dict) -> pd.DataFrame:
    missing = [c for c in FEATURES if c not in x]
    extra = [c for c in x.keys() if c not in FEATURES]

    if missing:
        raise ValueError(f"Missing required feature(s): {missing}")
    if extra:
        raise ValueError(f"Unexpected feature(s): {extra}. Allowed: {FEATURES}")

    row = {c: float(x[c]) for c in FEATURES}
    return pd.DataFrame([row], columns=FEATURES)

def predict_risk(wine_features: dict, threshold: float = FROZEN_THRESHOLD) -> dict:
    X = validate_and_build_df(wine_features)
    prob_high_risk = float(model.predict_proba(X)[:, 1][0])

    decision = "HIGH RISK" if prob_high_risk >= threshold else "LOW RISK"
    interpretation = (
        "Flag for preventive quality review before market release."
        if decision == "HIGH RISK"
        else "No preventive flag based on current chemical profile."
    )

    return {
        "risk_probability": prob_high_risk,
        "risk_decision": decision,
        "threshold_used": float(threshold),
        "interpretation": interpretation,
    }

# -----------------------------
# UI inputs
# -----------------------------
st.subheader("Input chemical features")

with st.form("wine_form"):
    col1, col2 = st.columns(2)

    with col1:
        fixed_acidity = st.number_input("fixed acidity", value=7.4, step=0.1)
        volatile_acidity = st.number_input("volatile acidity", value=0.70, step=0.01, format="%.2f")
        citric_acid = st.number_input("citric acid", value=0.00, step=0.01, format="%.2f")
        residual_sugar = st.number_input("residual sugar", value=1.9, step=0.1)
        chlorides = st.number_input("chlorides", value=0.076, step=0.001, format="%.3f")
        free_so2 = st.number_input("free sulfur dioxide", value=11.0, step=1.0)

    with col2:
        total_so2 = st.number_input("total sulfur dioxide", value=34.0, step=1.0)
        density = st.number_input("density", value=0.9978, step=0.0001, format="%.4f")
        ph = st.number_input("pH", value=3.51, step=0.01, format="%.2f")
        sulphates = st.number_input("sulphates", value=0.56, step=0.01, format="%.2f")
        alcohol = st.number_input("alcohol", value=9.4, step=0.1)

    submitted = st.form_submit_button("Predict risk")

# -----------------------------
# Prediction output
# -----------------------------
if submitted:
    wine = {
        "fixed acidity": fixed_acidity,
        "volatile acidity": volatile_acidity,
        "citric acid": citric_acid,
        "residual sugar": residual_sugar,
        "chlorides": chlorides,
        "free sulfur dioxide": free_so2,
        "total sulfur dioxide": total_so2,
        "density": density,
        "pH": ph,
        "sulphates": sulphates,
        "alcohol": alcohol,
    }

    try:
        out = predict_risk(wine, threshold=FROZEN_THRESHOLD)

        st.subheader("Result")
        st.write(f"**Decision:** {out['risk_decision']}")
        st.write(f"**Risk probability (risk=1):** {out['risk_probability']:.3f}")
        st.write(f"**Threshold used:** {out['threshold_used']:.3f}")
        st.info(out["interpretation"])

        with st.expander("Show input features"):
            st.dataframe(pd.DataFrame([wine], columns=FEATURES))

            # --- NEW: risk-related observations (reference-only)
            flags = detect_risk_flags(wine)
            st.markdown("### Risk-related observations (reference-only)")
            if flags:
                st.warning("Some inputs are outside typical dataset ranges:")
                for f in flags:
                    st.write(f"- {f}")
            else:
                st.success("All input values fall within typical ranges of the dataset.")

        st.caption(
            "Disclaimer: This tool estimates risk similarity based on patterns in the training dataset. "
            "It does not imply causality. The observations above highlight unusual inputs relative to typical ranges."
        )
    except Exception as e:
        st.error("Prediction failed. Please check inputs.")
        st.code(str(e))
