import streamlit as st
import pandas as pd
import numpy as np

# ── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CartIQ — AI Plug-in for Online Stores",
    page_icon="CartIQ",
    layout="wide",
    initial_sidebar_state="expanded"
)

import os

# ── Load External CSS ──────────────────────────────────────────────────────────
css_path = os.path.join(os.path.dirname(__file__), "style.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ── SVG Icons Helper ───────────────────────────────────────────────────────────
SVG_TARGET = '''<svg xmlns="http://www.w3.org/2000/svg" class="module-icon-svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>'''
SVG_USERS = '''<svg xmlns="http://www.w3.org/2000/svg" class="module-icon-svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" /></svg>'''
SVG_CHART = '''<svg xmlns="http://www.w3.org/2000/svg" class="module-icon-svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z" /></svg>'''
SVG_SHIELD = '''<svg xmlns="http://www.w3.org/2000/svg" class="module-icon-svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.956 11.956 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" /></svg>'''

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## CartIQ")
    st.markdown("*AI Plug-in for Online Stores*")
    st.markdown("---")
    
    if "page" not in st.session_state:
        st.session_state.page = "Dashboard Overview"
        
    pages = [
        "Dashboard Overview",
        "Smart Recommendations",
        "Customer Segmentation",
        "Demand Forecasting",
        "Fraud & Fake Review Detection",
    ]
    
    st.markdown("**Navigation**")
    for p in pages:
        b_type = "primary" if st.session_state.page == p else "secondary"
        if st.button(p, type=b_type, use_container_width=True):
            st.session_state.page = p
            st.rerun()
            
    page = st.session_state.page
    
    st.markdown("---")
    st.caption("CartIQ MVP — Sharia Entrepreneurship")

# ═══════════════════════════════════════════════════════════════════════════════
#  PAGE: DASHBOARD OVERVIEW
# ═══════════════════════════════════════════════════════════════════════════════
if page == "Dashboard Overview":
    st.markdown('<div class="hero-title">CartIQ</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">Give your online store a complete data-science team — in a single plug-in.</div>', unsafe_allow_html=True)
    
    st.markdown("### Four AI Modules Working Together")
    col1, col2, col3, col4 = st.columns(4)
    
    modules = [
        (SVG_TARGET, "Smart Recommendations", "Gradient Boosting + ANN", col1),
        (SVG_USERS, "Customer Segmentation", "K-Means Clustering", col2),
        (SVG_CHART, "Demand Forecasting", "Random Forest + Linear Reg.", col3),
        (SVG_SHIELD, "Fraud Detection", "Isolation Forest", col4),
    ]
    
    for svg, title, algo, col in modules:
        with col:
            st.markdown(f"""
            <div class="module-card">
                {svg}
                <div class="module-title">{title}</div>
                <div class="module-algo">{algo}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### Platform Metrics (Demo Data)")
    m1, m2, m3, m4 = st.columns(4)
    
    metrics = [
        ("Active Stores", "1,284", "+12% this month"),
        ("Avg Conversion Lift", "+23.4%", "vs. pre-CartIQ baseline"),
        ("Fraud Caught (30d)", "847", "transactions flagged"),
        ("Avg MRR / Store", "$89", "Starter → $299 Pro"),
    ]
    
    for col, (label, value, sub) in zip([m1, m2, m3, m4], metrics):
        with col:
            st.metric(label=label, value=value, delta=sub)
            
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Hide Lean Canvas inside an expander to reduce visual clutter
    with st.expander("View Lean Canvas Business Model", expanded=False):
        lean_data = {
            "Block": [
                "1. Customer Segments",
                "2. Problems",
                "3. Revenue Streams",
                "4. Solution",
                "5. Unique Value Proposition",
                "6. Channels",
                "7. Key Metrics",
                "8. Cost Structure",
                "9. Unfair Advantage",
            ],
            "Content": [
                "D2C growth-stage brands with 500+ monthly orders; no internal data team",
                "Generic storefronts → low conversion; poor demand forecast; fraud & fake reviews",
                "Tiered SaaS (Starter/Growth/Pro) + usage-based add-ons + managed service",
                "4 ML modules: Smart Reco, Customer Segmentation, Demand Forecast, Fraud Detection",
                '"Give your online store a complete data-science team in a single plug-in"',
                "Shopify App Store, WooCommerce Marketplace, content marketing, referral program",
                "MRR, active stores, avg conversion lift, churn rate, model accuracy",
                "Cloud/ML hosting, engineering salaries, sales & marketing, support",
                "Multi-model pipeline on aggregated cross-merchant data → compounding data moat",
            ]
        }
        st.dataframe(pd.DataFrame(lean_data), use_container_width=True, hide_index=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  PAGE: SMART RECOMMENDATIONS
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "Smart Recommendations":
    st.title("Smart Product Recommendations")
    st.caption("Algorithm: Gradient Boosting (XGBoost) + Artificial Neural Network (ANN) — Supervised Learning")
    
    st.markdown("""
    CartIQ analyses each customer's browsing and purchase history to generate a personalised 
    "For You" product feed, directly increasing conversion rates and average order value.
    """)
    st.markdown("---")
    
    # Adjusted column ratio for better whitespace management
    col1, col2 = st.columns([3, 7])
    
    with col1:
        st.markdown("#### Customer Profile")
        customer_id = st.selectbox("Select Customer", 
            ["CUST-001 (Loyal Buyer)", "CUST-002 (Bargain Hunter)", "CUST-003 (New Visitor)", "CUST-004 (High Spender)"])
        
        st.markdown("**Recent Purchases:**")
        if "Loyal" in customer_id:
            history = ["Running Shoes (×2)", "Sports Socks", "Water Bottle", "Fitness Tracker"]
            segment = "Loyal High-Spender"
        elif "Bargain" in customer_id:
            history = ["Discounted T-shirt", "Sale Sneakers", "Promo Bag"]
            segment = "Bargain Hunter"
        elif "New" in customer_id:
            history = ["Browsed Jackets", "Viewed Watches"]
            segment = "New Visitor"
        else:
            history = ["Premium Watch ($450)", "Designer Shoes ($320)", "Luxury Bag ($600)"]
            segment = "High Spender"
        
        for item in history:
            st.markdown(f"- {item}")
        
        st.markdown(f"**Segment:** {segment}")
        
        st.markdown("<br>", unsafe_allow_html=True)
        run_btn = st.button("Generate Recommendations", key="reco_btn")
    
    with col2:
        if run_btn:
            st.markdown("#### Personalised Product Feed")
            
            product_catalog = {
                "Loyal Buyer": [
                    ("Pro Running Shoes X2", "$129", 94, "Based on purchase pattern"),
                    ("Smart Hydration Pack", "$45", 88, "Frequently bought together"),
                    ("Fitness Tracker Pro", "$199", 81, "Upgrade from your current device"),
                    ("Performance Socks (6-pack)", "$28", 79, "Replenishment suggestion"),
                ],
                "Bargain Hunter": [
                    ("Flash Sale Jacket (-40%)", "$36", 95, "Active discount alert"),
                    ("Clearance Sneakers", "$29", 89, "Limited stock — your size available"),
                    ("Bundle Deal: Bag + Wallet", "$42", 83, "Best value this week"),
                    ("3-for-2 T-shirt Pack", "$30", 76, "Matches discount preference"),
                ],
                "New Visitor": [
                    ("Bestselling Winter Jacket", "$89", 90, "Top-rated by new customers"),
                    ("Entry-Level Smartwatch", "$79", 85, "Most viewed in your session"),
                    ("Starter Kit Bundle", "$55", 78, "Popular for first-time buyers"),
                    ("Casual Sneakers", "$65", 74, "Trending this week"),
                ],
                "High Spender": [
                    ("Luxury Watch Limited Edition", "$890", 97, "Matches premium purchase history"),
                    ("Designer Handbag New Arrival", "$750", 92, "Exclusive to Pro tier customers"),
                    ("Premium Leather Shoes", "$420", 87, "Completes your recent purchase"),
                    ("Premium Sunglasses", "$310", 82, "Curated for high-value profile"),
                ]
            }
            
            seg_key = customer_id.split("(")[1].replace(")", "")
            products = product_catalog.get(seg_key, product_catalog["Loyal Buyer"])
            
            for name, price, score, reason in products:
                bar_html = f"""
                <div class="result-card">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <strong style="color:#E2E8F0; font-size:1.05rem;">{name}</strong><br>
                            <small style="color:#94A3B8;">{reason}</small>
                        </div>
                        <div style="text-align:right;">
                            <div style="color:#4FC3F7; font-weight:700; font-size:1.15rem;">{price}</div>
                            <div style="background:rgba(255,255,255,0.05); border-radius:4px; height:8px; width:120px; margin-top:4px;">
                                <div style="background:linear-gradient(90deg,#2E75B6,#4FC3F7); border-radius:4px; height:8px; width:{score}%;"></div>
                            </div>
                            <small style="color:#60A5FA;">Match {score}%</small>
                        </div>
                    </div>
                </div>
                """
                st.markdown(bar_html, unsafe_allow_html=True)
        else:
            st.info("👈 Click **Generate Recommendations** to see the personalised feed for this customer.")

# ═══════════════════════════════════════════════════════════════════════════════
#  PAGE: CUSTOMER SEGMENTATION
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "Customer Segmentation":
    st.title("Customer Segmentation Engine")
    st.caption("Algorithm: K-Means Clustering — Unsupervised Learning")
    
    st.markdown("""
    CartIQ automatically groups your store's customers into behavioural segments,
    so you can run targeted marketing campaigns without hiring a data analyst.
    """)
    st.markdown("---")
    
    np.random.seed(42)
    n = 200
    
    segments = {
        "Loyal High-Spenders": {"n": 35, "spend": (250, 80), "freq": (12, 3)},
        "Bargain Hunters":     {"n": 60, "spend": (40, 15),  "freq": (8, 2)},
        "New Visitors":        {"n": 55, "spend": (70, 25),  "freq": (1, 0.5)},
        "At-Risk Churners":    {"n": 30, "spend": (90, 30),  "freq": (2, 1)},
        "Average Shoppers":    {"n": 20, "spend": (130, 40), "freq": (5, 2)},
    }
    
    rows = []
    for seg_name, cfg in segments.items():
        for _ in range(cfg["n"]):
            rows.append({
                "Segment":    seg_name,
                "Avg Spend ($)": max(5, np.random.normal(*cfg["spend"])),
                "Orders/Month":  max(1, np.random.normal(*cfg["freq"])),
            })
    
    df = pd.DataFrame(rows)
    
    col1, col2 = st.columns([4, 6])
    
    with col1:
        st.markdown("#### Segment Summary")
        summary = df.groupby("Segment").agg(
            Customers=("Segment", "count"),
            Avg_Spend=("Avg Spend ($)", "mean"),
            Avg_Orders=("Orders/Month", "mean"),
        ).round(1).reset_index()
        summary.columns = ["Segment", "Customers", "Avg Spend ($)", "Orders/Month"]
        st.dataframe(summary, use_container_width=True, hide_index=True)
        
        st.markdown("#### Recommended Actions")
        actions = {
            "Loyal High-Spenders": "VIP early-access offers",
            "Bargain Hunters":     "Flash sales & bundle deals",
            "New Visitors":        "Welcome discount sequence",
            "At-Risk Churners":    "Win-back campaign with offer",
            "Average Shoppers":    "Upsell complementary products",
        }
        for seg, action in actions.items():
            st.markdown(f"- **{seg}**<br><small style='color:#94A3B8;'>→ {action}</small>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### Customer Cluster Map")
        st.scatter_chart(
            df,
            x="Orders/Month",
            y="Avg Spend ($)",
            color="Segment",
            size=40,
        )

# ═══════════════════════════════════════════════════════════════════════════════
#  PAGE: DEMAND FORECASTING
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "Demand Forecasting":
    st.title("Demand Forecasting")
    st.caption("Algorithm: Random Forest + Linear Regression — Supervised Learning")
    
    st.markdown("""
    CartIQ predicts next-week or next-month product demand per SKU,
    helping you avoid costly overstock and stockout situations.
    """)
    st.markdown("---")
    
    col1, col2 = st.columns([3, 7])
    
    with col1:
        st.markdown("#### Forecast Settings")
        sku = st.selectbox("Select Product (SKU)", [
            "SKU-001 — Running Shoes",
            "SKU-002 — Winter Jacket",
            "SKU-003 — Smart Watch",
            "SKU-004 — Yoga Mat",
        ])
        
        horizon = st.slider("Forecast Horizon (weeks)", 1, 8, 4)
        
        seasonality = st.toggle("Include Seasonality Effect", value=True)
        promotions  = st.toggle("Include Promo Calendar", value=False)
        
        st.markdown("<br>", unsafe_allow_html=True)
        run_forecast = st.button("Run Forecast", key="forecast_btn")
    
    with col2:
        if run_forecast:
            st.markdown("#### Demand Forecast Results")
            
            base_demands = {
                "SKU-001 — Running Shoes": 120,
                "SKU-002 — Winter Jacket": 85,
                "SKU-003 — Smart Watch":   60,
                "SKU-004 — Yoga Mat":      95,
            }
            
            base = base_demands[sku]
            weeks = [f"Week {i+1}" for i in range(horizon)]
            
            np.random.seed(10)
            forecast = [base + int(np.random.normal(0, 10)) + (5*i if seasonality else 0) + (30 if promotions and i == 2 else 0) for i in range(horizon)]
            lower_ci  = [max(0, f - 15) for f in forecast]
            upper_ci  = [f + 15 for f in forecast]
            
            chart_data = pd.DataFrame({
                "Week": weeks,
                "Forecast": forecast,
                "Lower CI": lower_ci,
                "Upper CI": upper_ci,
            })
            
            st.line_chart(chart_data.set_index("Week")[["Forecast", "Lower CI", "Upper CI"]])
            
            total = sum(forecast)
            current_stock = 200 # Fixed for demo simplicity
            reorder_point = int(min(forecast) * 0.5)
            recommended_order = max(0, total - current_stock + 50)
            
            m1, m2, m3 = st.columns(3)
            m1.metric("Total Forecast (units)", total)
            m2.metric("Recommended Order", f"{recommended_order}")
            m3.metric("Reorder Point", f"{reorder_point}")
        else:
            st.info("👈 Configure the settings and click **Run Forecast** to generate predictions.")

# ═══════════════════════════════════════════════════════════════════════════════
#  PAGE: FRAUD DETECTION
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "Fraud & Fake Review Detection":
    st.title("Fraud & Fake Review Detection")
    st.caption("Algorithm: Isolation Forest — Unsupervised Learning")
    
    st.markdown("""
    CartIQ flags anomalous transactions and suspicious review patterns in real time,
    protecting your revenue and building buyer trust — before a single sale is lost.
    """)
    st.markdown("---")
    
    tab1, tab2 = st.tabs(["Transaction Fraud Scanner", "Fake Review Detector"])
    
    with tab1:
        st.markdown("#### Transaction Analyser")
        
        col1, col2 = st.columns(2)
        with col1:
            amount    = st.number_input("Transaction Amount ($)", min_value=1, value=250)
            country   = st.selectbox("Billing Country", ["Indonesia", "United States", "Nigeria", "Singapore", "Russia"])
            hour      = st.slider("Hour of Transaction (24h)", 0, 23, 14)
        with col2:
            new_acct  = st.toggle("New Account (< 7 days old)", value=False)
            vpn       = st.toggle("VPN / Proxy Detected", value=False)
            attempts  = st.number_input("Failed Login Attempts (today)", min_value=0, value=0)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Analyse Transaction", key="fraud_btn"):
            score = 0
            flags = []
            if amount > 500: score += 30; flags.append("High-value transaction")
            if country in ["Nigeria", "Russia"]: score += 40; flags.append(f"High-risk billing country ({country})")
            if hour < 3 or hour > 22: score += 20; flags.append("Unusual transaction hour")
            if new_acct: score += 25; flags.append("Brand-new account")
            if vpn: score += 35; flags.append("VPN/Proxy usage detected")
            if attempts >= 3: score += 30; flags.append(f"{attempts} failed login attempts today")
            
            score = min(score, 100)
            
            st.markdown("---")
            st.markdown("#### Isolation Forest Analysis Result")
            
            if score >= 60:
                st.error(f"HIGH RISK — Anomaly Score: {score}/100")
                badge = '<span class="badge badge-red">FLAGGED</span>'
                action = "Transaction **BLOCKED** for manual review. Customer notified via email."
            elif score >= 30:
                st.warning(f"MEDIUM RISK — Anomaly Score: {score}/100")
                badge = '<span class="badge badge-orange">REVIEW</span>'
                action = "Transaction held for **2-hour review**. Additional verification sent to customer."
            else:
                st.success(f"LOW RISK — Anomaly Score: {score}/100")
                badge = '<span class="badge badge-green">CLEAR</span>'
                action = "Transaction **APPROVED** and processed normally."
            
            st.markdown(f"**Status:** {badge}", unsafe_allow_html=True)
            st.markdown(f"**Action:** {action}")
    
    with tab2:
        st.markdown("#### Fake Review Analyser")
        
        review_text = st.text_area("Paste Review Text", 
            value="Amazing product!! Totally worth it. Best purchase ever. 5 stars. Love it. Great great great!!!",
            height=100)
        
        reviewer_age    = st.number_input("Reviewer Account Age (days)", min_value=0, value=2)
        total_reviews   = st.number_input("Total Reviews by This User", min_value=1, value=47)
        verified_purchase = st.toggle("Verified Purchase", value=False)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Analyse Review", key="review_btn"):
            score = 0
            flags = []
            
            exclamations = review_text.count('!')
            caps_ratio   = sum(1 for c in review_text if c.isupper()) / max(len(review_text), 1)
            word_count   = len(review_text.split())
            repetitions  = len(set(review_text.lower().split())) / max(word_count, 1)
            
            if exclamations > 3: score += 20; flags.append(f"Excessive exclamation marks ({exclamations})")
            if caps_ratio > 0.15: score += 15; flags.append("Abnormally high capitalisation ratio")
            if repetitions < 0.5: score += 25; flags.append("High repetition — low vocabulary diversity")
            if word_count < 15: score += 15; flags.append("Suspiciously short review")
            
            if reviewer_age < 7: score += 30; flags.append(f"New account ({reviewer_age} days old)")
            if total_reviews > 20 and reviewer_age < 30: score += 30; flags.append("Unusually high review volume for account age")
            if not verified_purchase: score += 20; flags.append("Not a verified purchase")
            
            score = min(score, 100)
            
            st.markdown("---")
            st.markdown("#### Isolation Forest Analysis Result")
            
            if score >= 60:
                st.error(f"LIKELY FAKE — Suspicion Score: {score}/100")
                action = "Review **HIDDEN** pending manual moderation."
            elif score >= 30:
                st.warning(f"SUSPICIOUS — Suspicion Score: {score}/100")
                action = "Review **FLAGGED** — shown with low-trust badge to buyers."
            else:
                st.success(f"LOOKS AUTHENTIC — Suspicion Score: {score}/100")
                action = "Review **APPROVED** and published normally."
            
            st.markdown(f"**Action:** {action}")
