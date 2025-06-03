import streamlit as st
import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI-Powered Analytics Developer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS ---
# Current year for footer
current_year = datetime.date.today().year

custom_css = f"""
<style>
    /* General */
    body {{
        font-family: 'Arial', sans-serif; 
    }}

    /* Headers */
    h1, h2, h3 {{
        color: #1f77b4; /* Blue headers */
    }}
    
    .section-header {{
        color: #1f77b4;
        font-size: 2em;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
    }}

    .orange-accent-border {{
        border: 2px solid #ff7f0e !important;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
    }}

    .profile-img-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
    }}
    .profile-img {{
        width: 150px;
        height: 150px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #ff7f0e;
    }}

    .project-card {{
        background-color: #f9f9f9;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease-in-out;
    }}
    .project-card:hover {{
        transform: translateY(-5px);
    }}
    /* Styling for the div that holds st.image or the placeholder */
    div[data-testid="stVerticalBlock"] > div[style*="flex-direction: column;"] > div[data-testid="stImage"] {{
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100%; 
    }}
    div[data-testid="stVerticalBlock"] > div[style*="flex-direction: column;"] > div[data-testid="stImage"] > img {{
        max-height: 170px; 
        border-radius: 4px; 
        object-fit: contain; 
    }}
    .project-image-placeholder {{ 
        width: 100%;
        height: 170px; 
        background-color: #e0e0e0;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 4px;
        font-weight: bold;
        color: #555;
    }}

    .skill-tag {{
        background-color: #ff7f0e;
        color: white;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 0.9em;
        margin-right: 5px;
        margin-bottom: 5px;
        display: inline-block;
    }}

    .service-tier {{
        border: 1px solid #ddd;
        border-top: 5px solid #ff7f0e;
        border-radius: 8px;
        padding: 20px;
        text-align: center;
        height: 100%; 
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }}
    .service-tier h3 {{
        color: #1f77b4;
        margin-top: 0;
    }}
    .service-tier ul {{
        text-align: left;
        padding-left: 20px;
        list-style-position: inside;
    }}

    .rainbow-divider {{
        height: 5px;
        background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
        border: none;
        margin-top: 5px;
        margin-bottom: 25px;
    }}
    .orange-divider {{
        border-top: 3px solid #ff7f0e;
        margin-top: 5px;
        margin-bottom: 25px;
    }}
    .blue-divider {{
        border-top: 3px solid #1f77b4;
        margin-top: 5px;
        margin-bottom: 25px;
    }}
    .green-divider {{
        border-top: 3px solid #2ca02c;
        margin-top: 5px;
        margin-bottom: 25px;
    }}
    
    .stExpander {{
        border: 1px solid #ddd;
        border-radius: 8px;
    }}
    .stExpander header {{
        font-size: 1.2em;
        font-weight: bold;
        background-color: #f0f2f6;
    }}

    .mermaid {{
        text-align: center;
        margin-top: 10px;
        margin-bottom: 10px;
    }}
    
    .footer {{
        text-align: center;
        padding: 20px;
        color: #777;
        font-size: 0.9em;
    }}

</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- HEADER SECTION ---
your_name = "Sujit Halder"
profile_pic_url = "https://i.postimg.cc/Cx2Bg757/B6636-B29-1.jpg" 

# Social Media Links HTML
social_media_html = """
<div style="text-align: right; margin-bottom: 5px; font-size: 0.9em;">
    <a href="https://www.linkedin.com/in/sujithalder/" target="_blank" style="margin-left: 10px; text-decoration: none; color: #1f77b4; font-weight: bold;">LinkedIn</a>
    <span style="color: #ccc; margin-left: 5px; margin-right: 5px;">|</span>
    <a href="https://www.facebook.com/sujit.halder.58/" target="_blank" style="text-decoration: none; color: #1f77b4; font-weight: bold;">Facebook</a>
    <span style="color: #ccc; margin-left: 5px; margin-right: 5px;">|</span>
    <a href="https://www.youtube.com/watch?v=8koNl8m7r6M" target="_blank" style="text-decoration: none; color: #1f77b4; font-weight: bold;">YouTube</a>
</div>
"""

col1, col2 = st.columns([1, 3]) # Profile pic on left, details on right

with col1:
    st.markdown(f"""
    <div class="profile-img-container">
        <img src="{profile_pic_url}" class="profile-img" alt="Profile Photo of {your_name}">
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(social_media_html, unsafe_allow_html=True) # Add social media links first
    st.markdown(f"<h1 style='color: #1f77b4; margin-bottom: 0px; margin-top: 0px;'>{your_name}</h1>", unsafe_allow_html=True) # Name
    st.markdown("### Prompt Engineer & Low-Code Analytics Developer") # Tagline
    st.markdown("⚡ **Transforming business questions into functional tools using AI-assisted development**") # Value Proposition
    st.markdown("""
    - 🚀 15+ deployed Streamlit applications
    - 💡 AI-powered prototyping specialist
    - 📊 Business analytics translator
    """) # Bullet Points

st.markdown("---")

# --- UNIQUE VALUE PROPOSITION SECTION ---
with st.expander("✨ MY UNIQUE APPROACH", expanded=True):
    st.markdown("""
    My process leverages the power of AI to rapidly prototype and develop analytical applications. 
    This means faster delivery, iterative feedback, and solutions highly tailored to your specific needs.
    """)

    mermaid_diagram = """
    <div class="mermaid">
        graph LR
        A[Client Problem] --> B(Prompt Engineering);
        B --> C[AI-Generated Code];
        C --> D[Streamlit Application];
        D --> E[Business Insights];
    </div>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <script>
        if (typeof mermaid !== 'undefined') {
            mermaid.initialize({ startOnLoad: true });
            mermaid.contentLoaded(); 
        } else {
            document.addEventListener('DOMContentLoaded', function () {
                if (typeof mermaid !== 'undefined') {
                    mermaid.initialize({ startOnLoad: true });
                    mermaid.contentLoaded();
                }
            });
        }
    </script>
    """
    st.components.v1.html(mermaid_diagram, height=300, scrolling=False)
    st.success("✅ Deliver functional analytics tools **5x faster** than traditional development")

# --- PROJECTS SHOWCASE ---
st.markdown("<div class='section-header'>🚀 Featured Projects</div>", unsafe_allow_html=True)
st.markdown("<div class='rainbow-divider'></div>", unsafe_allow_html=True)

projects_data = [
    {
        "title": "Corporate Data Analytics Tool",
        "description": "Versatile tool for uploading and analyzing CSV, Excel, or PDF data files. Features include sidebar uploads, PDF table selection, data exploration/cleaning options, and a toggle for dark mode.",
        "skills": ["Streamlit", "Data Upload (CSV, Excel, PDF)", "UI/UX Design", "File Parsing"],
        "image_src": "https://i.postimg.cc/VNxcmrX2/Corporate-data-analytics-tool-interface.jpg", 
        "image_text": "Corporate Data Tool UI", 
        "live_app_url": "https://data-analytics-tools-hpa6376wld7jjgdafdfacj.streamlit.app/"
    },
    {
        "title": "Sales Analytics Dashboard",
        "description": "Geolift data analysis with performance metrics. Interactive visualizations for sales trends, regional performance, and product insights.",
        "skills": ["Streamlit", "Pandas", "Plotly", "Data Cleaning"],
        "image_src": None, 
        "image_text": "Sales Dashboard UI",
        "live_app_url": "#" 
    },
    {
        "title": "Algorithmic Trading Interface",
        "description": "Simulated trading system with live dashboard. Backtesting strategies, portfolio tracking, and risk assessment tools.",
        "skills": ["Python", "Data Visualization", "Financial Analysis", "API Integration"],
        "image_src": None,
        "image_text": "Trading Interface Mockup",
        "live_app_url": "#" 
    },
    {
        "title": "Logistics Optimization Tool",
        "description": "Route efficiency and shipment performance analytics. Geospatial analysis for delivery routes and cost reduction opportunities.",
        "skills": ["Data Modeling", "GeoPandas", "Cost Analysis", "Optimization"],
        "image_src": None,
        "image_text": "Logistics Map View",
        "live_app_url": "#" 
    }
]

for i, project in enumerate(projects_data):
    st.markdown(f"<div class='project-card'>", unsafe_allow_html=True)
    col_img, col_details = st.columns([1, 2]) 
    with col_img:
        if project.get("image_src") and project["image_src"] != "#" and project["image_src"] is not None:
            st.image(
                project["image_src"], 
                use_container_width=True, 
                caption="" 
            ) 
        else:
            st.markdown(f"""
                <div class="project-image-placeholder">
                    {project.get('image_text', 'Project Image')}
                </div>
            """, unsafe_allow_html=True)

    with col_details:
        st.markdown(f"<h3>{project['title']}</h3>", unsafe_allow_html=True)
        st.markdown(project['description'])
        
        skills_html = "".join([f"<span class='skill-tag'>{skill}</span>" for skill in project['skills']])
        st.markdown(skills_html, unsafe_allow_html=True)
        
        if project["live_app_url"] and project["live_app_url"] != "#":
            st.markdown(f"""
                <a href="{project['live_app_url']}" target="_blank" 
                   style="background-color: #ff7f0e; color: white; padding: 8px 15px; text-decoration: none; border-radius: 5px; display: inline-block; margin-top: 10px;">
                   View Live App
                </a>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"<p style='margin-top:10px;'><em>Live app link for {project['title']} coming soon.</em></p>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
    if i < len(projects_data) - 1:
        st.markdown("<hr style='border-top: 1px solid #ddd; margin: 20px 0;'>", unsafe_allow_html=True)

# --- SERVICE PACKAGES ---
st.markdown("<div class='section-header'>💼 Service Packages</div>", unsafe_allow_html=True)
st.markdown("<div class='orange-divider'></div>", unsafe_allow_html=True)

col_tier1, col_tier2, col_tier3 = st.columns(3)

def service_tier_html(title, price, features, cta_text, cta_link="#contact"):
    features_html = "".join([f"<li>{feature}</li>" for feature in features])
    return f"""
    <div class="service-tier">
        <h3>{title}</h3>
        <p style="font-size: 1.5em; font-weight: bold; color: #ff7f0e;">{price}</p>
        <ul>{features_html}</ul>
        <div style="margin-top: auto; padding-top:10px;">
            <a href="{cta_link}" style="text-decoration:none; color: #fff; background-color: #1f77b4; padding: 10px 15px; border-radius: 5px; display: inline-block;">
                {cta_text}
            </a>
        </div>
    </div>
    """

with col_tier1:
    st.markdown(service_tier_html(
        "🚀 Prompt-to-App Basic", "$149",
        ["Simple analytics dashboard", "1 data source integration", "3 visualization types"],
        "Select Basic"
    ), unsafe_allow_html=True)

with col_tier2:
    st.markdown(service_tier_html(
        "🚀 Pro Business Automator", "$349",
        ["Multi-source data pipeline", "Interactive reporting", "Custom business logic"],
        "Select Pro"
    ), unsafe_allow_html=True)

with col_tier3:
    st.markdown(service_tier_html(
        "🚀 Enterprise Solution", "Custom",
        ["End-to-end workflow automation", "Database integration", "Advanced analytics & AI models"],
        "Contact Us"
    ), unsafe_allow_html=True)

# --- PROCESS DEMO ---
st.markdown("<div class='section-header'>🔧 How It Works</div>", unsafe_allow_html=True)
st.markdown("<div class='blue-divider'></div>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["1. Share Requirements", "2. AI Development", "3. Refinement", "4. Deployment"])

with tab1:
    st.subheader("You describe your analytical need:")
    st.code("""
    Example:
    "Build a dashboard showing sales trends by region and product category for the last quarter. 
    Data is in a CSV file. I need to see YoY growth and top performing products."
    """, language="text")
    st.markdown("We discuss the core problem, data sources, and desired outcomes.")

with tab2:
    st.subheader("AI-Assisted Code Generation & Prototyping:")
    st.markdown("I use advanced prompt engineering techniques with AI code generation models to rapidly create the foundational application structure and analytical components.")
    st.code("""
    Example Prompt Snippet (Conceptual):
    "User wants a Streamlit dashboard with pandas for data manipulation and Plotly for visualizations.
    Input: CSV file with columns ['Date', 'Region', 'Product', 'Sales'].
    Tasks:
    1. Load data, clean dates.
    2. Create a line chart for overall sales trend.
    3. Create a bar chart for sales by region.
    4. Allow filtering by date range and region."
    """, language="text")

with tab3:
    st.subheader("Iterative Refinement & Customization:")
    st.markdown("We review the AI-generated prototype. I then refine the code, add custom logic, and tailor the UI/UX to your exact specifications. This phase involves collaborative feedback.")
    collaboration_img_url = "https://cdn.pixabay.com/photo/2017/07/31/22/30/cat-2560377_640.jpg" 
    st.image(collaboration_img_url, caption="Collaborative Refinement (Placeholder)", width=300)

with tab4:
    st.subheader("Deployment & Handover:")
    st.markdown("Once finalized, your application is deployed to a secure Streamlit sharing environment or your preferred platform.")
    st.success("🚀 Your AI-powered analytics tool is live! Example: `https://your-app-name.streamlit.app`")
    st.balloons()

# --- CONTACT SECTION ---
st.markdown("<a id='contact'></a>", unsafe_allow_html=True) 
st.markdown("<div class='section-header'>📬 Let's Connect</div>", unsafe_allow_html=True)
st.markdown("<div class='green-divider'></div>", unsafe_allow_html=True)

formsubmit_email = "your_formsubmit_email@example.com" # <<< USER ACTION: REPLACE THIS

st.markdown(f"""
<div class="orange-accent-border">
    <h4>Interested in transforming your data into actionable insights? Reach out!</h4>
    <form action="https://formsubmit.co/{formsubmit_email}" method="POST">
        <input type="text" name="name" placeholder="Your Name" required 
               style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;">
        <input type="email" name="email" placeholder="Your Email" required
               style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;">
        <textarea name="message" placeholder="Your Message" required
                  style="width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px; min-height: 100px; box-sizing: border-box;"></textarea>
        <input type="hidden" name="_captcha" value="false"> 
        <button type="submit" 
                style="background-color: #ff7f0e; color: white; border: none; padding: 10px 20px; border-radius: 5px; font-weight: bold; cursor: pointer;">
            Send Message
        </button>
    </form>
</div>
""", unsafe_allow_html=True)
st.markdown(f"<p style='font-size:0.8em; text-align:center;'>Note: The contact form uses <a href='https://formsubmit.co/' target='_blank'>Formsubmit.co</a>. Remember to replace <code>{formsubmit_email}</code> with your actual email and activate it on Formsubmit.</p>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<hr style='border-top: 1px solid #ddd; margin: 40px 0 20px 0;'>", unsafe_allow_html=True)
st.markdown(f"""
<div class="footer">
    © {current_year} | {your_name} - AI-Powered Development Portfolio | Updated monthly
</div>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div style="font-size:0.8em; text-align:center; color: #aaa; margin-top: 10px; margin-bottom: 20px;">
        Cat image in 'Refinement' tab is illustrative. Other placeholder images from Pixabay.
    </div>
    """, unsafe_allow_html=True
)