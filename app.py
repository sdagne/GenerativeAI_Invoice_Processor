

import streamlit as st
import os
from Fileload import INPUT_DIR, seen, save_seen, ensure_schema
from email_notify import send_email
from graphviz import Digraph

# --- Page Config ---
st.set_page_config(page_title="Invoice Processor Agent", layout="wide")
st.title("📄 Invoice Processor Agent")


#----------------------------------------------------------
st.markdown(
    """
    <style>
   
     /* Dark background for the app */
    .stApp {
        background-color: #125589;
        color: #ffffff;
    }    
    

    /* ✅ "Upload Invoice Image" label → white */
    .stFileUploader > label {
        color: white !important;
        font-weight: bold;
    }
    
    
    
    /* Keep your dark background for the main app */
    .stApp {
        background-color: #125589;
        color: #ffffff;
    }

header {
    background-color:  #7b2cbf !important; /*  blue */
    height: 40px;
}
   
    /* File uploader */
    .css-1r6slb0 {
        background-color: #125589;
        color: white;
        border-radius: 20px;
    }
    
    /* Alerts */
    .stAlert {
        border-radius: 10px;
        padding: 10px;
        color: #ffffff;
        background-color: #333333;
    }
    
    /* Labels */
    .stTextInput > label {
        color: white !important;
        font-weight: bold;
    }
   
    /* Buttons */
    .stButton>button {
        background-color: #dda0dd !important;
        color: #ffffff !important;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Footer ---
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #1a1a1a;
        color: #cccccc;
        text-align: center;
        padding: 8px 0;
        font-size: 14px;
        border-top: 1px solid #333333;
        z-index: 100;
    }
    .footer a {
        color: #ff99cc;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    <div class="footer">
        Developed by <a href="https://github.com/sdagne" target="_blank">Shewan Dagne</a> &bull; as part of the Generative AI Learning Project
    </div>
    """,
    unsafe_allow_html=True
)






# --- Ensure input folder & DB exist ---
ensure_schema()
os.makedirs(INPUT_DIR, exist_ok=True)

# --- Upload Invoice ---
uploaded_file = st.file_uploader("Upload Invoice Image", type=["png", "jpg", "jpeg"])
file_path = None
if uploaded_file is not None:
    file_path = os.path.join(INPUT_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    seen.add(uploaded_file.name)
    save_seen(seen)
    st.success(f"✅ File uploaded: {uploaded_file.name}")

# --- Email input + send button ---
recipient_email = st.text_input("Recipient Email")
if st.button("Send Email"):
    if recipient_email:
        ok = send_email(
            "shewan.dagne1@gmail.com",
            recipient_email,
            "Invoice Processed",
            "Your invoice has been processed successfully."
        )
        if ok:
            st.success(f"📧 Email sent to: {recipient_email}")
        else:
            st.error("❌ Failed to send email. Check server logs.")
    else:
        st.warning("⚠️ Please enter a recipient email first.")

# --- Knowledge graph + invoice preview side by side ---
st.subheader("📊 Invoice Pipeline")
col_left, col_right = st.columns([2, 1])  # left: graph, right: invoice

# --- Knowledge Graph ---
with col_left:
    dot = Digraph(graph_attr={"rankdir": "LR"})  # horizontal layout

    # Colored nodes in pink shades
    dot.node("WATCH", "WATCH", style="filled", fillcolor="#eadde3")
    dot.node("OCR", "OCR", style="filled", fillcolor="#99ffc2")
    dot.node("CLEAN", "CLEAN", style="filled", fillcolor="#ff66b3")
    dot.node("EXTRACT", "EXTRACT", style="filled", fillcolor="#ff3399")
    dot.node("VALIDATE", "VALIDATE", style="filled", fillcolor="#ff007f")
    dot.node("PERSIST", "PERSIST", style="filled", fillcolor="#e60073")
    dot.node("NOTIFY", "NOTIFY", style="filled", fillcolor="#b3005c")

    edges = [
        ("WATCH", "OCR"),
        ("OCR", "CLEAN"),
        ("CLEAN", "EXTRACT"),
        ("EXTRACT", "VALIDATE"),
        ("VALIDATE", "PERSIST"),
        ("PERSIST", "NOTIFY"),
    ]
    for edge in edges:
        dot.edge(*edge)

    st.graphviz_chart(dot)

# --- Invoice Preview ---
with col_right:
    if file_path:
        st.image(
            file_path,
            caption="Uploaded Invoice",
            width=227  # ≈ 6 cm
        )
        
        

#print("Graphviz imported successfully")
#dot = Digraph(comment='Test Graph')
#dot.node('A', 'Start')
#dot.node('B', 'Process')
#dot.edge('A', 'B')
#print(dot.source)  # Prints DOT source