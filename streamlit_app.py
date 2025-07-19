import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

# Try to import plotly, fallback to matplotlib if not available
try:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False
    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as patches
        MATPLOTLIB_AVAILABLE = True
    except ImportError:
        MATPLOTLIB_AVAILABLE = False

# Page configuration
st.set_page_config(
    page_title="Andre's Automation Portfolio",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .project-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
    }
    .tech-stack {
        background-color: #f0f2f6;
        padding: 0.5rem 1rem;
        border-radius: 15px;
        display: inline-block;
        margin: 0.2rem;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("AI Portfolio")
page = st.sidebar.selectbox(
    "Navigate to:",
    ["Executive Overview", "1. AI Email Assistant", "2. Smart Lead Router", 
     "3. OCR + Slack AI Bot", "4. AI Blog Writing Tool", 
     "5. Alibaba Lead Classifier", "6. Outlook Email Classifier"]
)

def create_flowchart(nodes, connections, title):
    """Create a flowchart with available visualization library"""
    if PLOTLY_AVAILABLE:
        fig = go.Figure()
        
        # Add nodes
        for i, (node, color) in enumerate(nodes):
            fig.add_trace(go.Scatter(
                x=[i % 4], y=[i // 4],
                mode='markers+text',
                marker=dict(size=80, color=color),
                text=node,
                textposition="middle center",
                textfont=dict(size=10, color='white'),
                name=node,
                showlegend=False
            ))
        
        # Add connections (simplified for visualization)
        for start, end in connections:
            start_idx = next(i for i, (node, _) in enumerate(nodes) if node == start)
            end_idx = next(i for i, (node, _) in enumerate(nodes) if node == end)
            
            fig.add_trace(go.Scatter(
                x=[start_idx % 4, end_idx % 4],
                y=[start_idx // 4, end_idx // 4],
                mode='lines',
                line=dict(color='gray', width=2),
                showlegend=False
            ))
        
        fig.update_layout(
            title=dict(text=title, x=0.5, font=dict(size=16)),
            xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
            yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
            height=400,
            margin=dict(l=20, r=20, t=60, b=20)
        )
        
        return fig
    else:
        # Fallback: Create a text-based flowchart
        return create_text_flowchart(nodes, connections, title)

def create_text_flowchart(nodes, connections, title):
    """Create a text-based flowchart representation"""
    flowchart_text = f"## {title}\n\n"
    
    # Create a simple text representation
    flowchart_text += "```\n"
    for i, (node, _) in enumerate(nodes):
        if i == 0:
            flowchart_text += f"┌─ {node}\n"
        else:
            flowchart_text += f"├─ {node}\n"
            
        # Add connections
        for start, end in connections:
            if start == node:
                flowchart_text += f"│  └─→ {end}\n"
    
    flowchart_text += "```\n"
    return flowchart_text

def create_simple_chart(data, chart_type="bar", title="Chart"):
    """Create simple charts with fallback options"""
    if PLOTLY_AVAILABLE:
        if chart_type == "bar":
            fig = go.Figure(data=[go.Bar(x=data.index, y=data.values)])
        elif chart_type == "line":
            fig = go.Figure(data=[go.Scatter(x=data.index, y=data.values, mode='lines+markers')])
        elif chart_type == "pie":
            fig = go.Figure(data=[go.Pie(labels=data.index, values=data.values)])
        
        fig.update_layout(title=title, height=300)
        return fig
    else:
        # Return data for simple display
        return data

def generate_sample_metrics():
    """Generate sample metrics for demonstration"""
    return {
        'emails_processed': "N/A",
        'leads_qualified': "N/A",
        'time_saved': "N/A",
        'accuracy_rate': "N/A",
        'documents_processed': "N/A",
        'slack_interactions': "N/A"
    }

# Main content based on selected page
if page == "Executive Overview":
    st.markdown('<h1 class="main-header">AI Automation Portfolio</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Strategic Overview
    This AI automation projects portfolio delivers measurable ROI through intelligent process automation, 
    reducing manual workload while improving accuracy and response times.
    """)
    
    # Key Metrics Dashboard
    metrics = generate_sample_metrics()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Emails Processed", f"{int(metrics['emails_processed']):,}", "↑ 23%")
    with col2:
        st.metric("Leads Qualified", f"{int(metrics['leads_qualified']):,}", "↑ 34%")
    with col3:
        st.metric("Hours Saved/Month", f"{int(metrics['time_saved'])}", "↑ 45%")
    with col4:
        st.metric("AI Accuracy", f"{int(metrics['accuracy_rate'])}%", "↑ 2.1%")
    
    st.markdown("---")
    
    # Project Portfolio Overview
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Email Intelligence Suite
        - **AI Email Assistant**: Automated lead qualification
        - **Smart Lead Router**: Multi-channel lead management  
        - **Outlook Classifier**: Email thread analysis
        
        **ROI Impact**: 67% reduction in manual email processing
        """)
        
        st.markdown("""
        ### Document Intelligence
        - **OCR + Slack Bot**: Smart document processing
        - **AI Blog Tool**: Automated content generation
        
        **ROI Impact**: 78% faster document processing
        """)
    
    with col2:
        st.markdown("""
        ### Lead Generation & Qualification
        - **Alibaba Classifier**: B2B lead identification
        - **Multi-platform Integration**: Unified lead scoring
        
        **ROI Impact**: 156% increase in qualified leads
        """)
        
        # Technology Stack Overview
        st.markdown("""
        ### Technology Stack
        """)
        
        tech_stack = [
            "Python", "Streamlit", "OpenAI GPT", "LLaMA", "Gmail API",
            "Microsoft Graph", "Google Sheets", "Slack API", "n8n",
            "Tesseract OCR", "Google Vision", "HubSpot CRM", "Selenium"
        ]
        
        for tech in tech_stack:
            st.markdown(f'<span class="tech-stack">{tech}</span>', unsafe_allow_html=True)

elif page == "1. AI Email Assistant":
    st.title("AI Email Assistant")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        ### Project Overview
        Automatically identify incoming emails, read and produce proper replies based on an established prompt.
        
        ### Key Features
        - **Gmail Integration**: Real-time email monitoring
        - **AI Integration**: Smart system for auto replies
        - **Auto-logging**: Direct Google Sheets integration
        - **Auto-categorization**: Categorize each email based on priority           
        - **Web Interface**: Streamlit dashboard
        
        ### Business Impact
        - **Time Savings**
        - **Auto Replies**
        - **Response Time**
        """)
    
    with col2:
        # Create flowchart
        nodes = [
            ("Gmail API", "#1f77b4"),
            ("Fetch Emails", "#ff7f0e"),
            ("AI Classifier", "#2ca02c"),
            ("Lead Scoring", "#d62728"),
            ("Google Sheets", "#9467bd"),
            ("Streamlit UI", "#8c564b")
        ]
        
        connections = [
            ("Gmail API", "Fetch Emails"),
            ("Fetch Emails", "AI Classifier"),
            ("AI Classifier", "Lead Scoring"),
            ("Lead Scoring", "Google Sheets"),
            ("Google Sheets", "Streamlit UI")
        ]
        
        fig = create_flowchart(nodes, connections, "AI Email Assistant Workflow")
        if PLOTLY_AVAILABLE:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.markdown(fig)
    
    # Technical Implementation
    st.markdown("### Technical Architecture")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        **Data Ingestion**
        - Gmail API authentication
        - Real-time email polling
        - Attachment handling
        """)
    
    with col2:
        st.markdown("""
        **AI Processing**
        - OpenAI GPT-4 classification
        - Custom prompt engineering
        - OpenAI GPT-4 language processing
        """)
    
    with col3:
        st.markdown("""
        **Output & Storage**
        - Google Sheets API
        - Automated logging
        - Dashboard visualization
        """)

elif page == "2. Smart Lead Router":
    st.title("Smart Lead Router")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        ### Project Overview
        Multi-channel lead intake system with AI-powered routing 
        and automatic CRM integration.
        
        ### Key Features
        - **Multiple Input Sources**: Web forms, email, webhooks
        - **AI Intent Detection**: Job title and industry classification
        - **Smart Routing**: Automated team assignment
        - **CRM Integration**: HubSpot auto-contact creation
        
        ### Business Impact
        - **Lead Processing**
        - **Team Efficiency**
        - **Data Quality**
        """)
    
    with col2:
        nodes = [
            ("Web Form", "#1f77b4"),
            ("Email Input", "#ff7f0e"),
            ("Webhook", "#2ca02c"),
            ("n8n Router", "#d62728"),
            ("AI Intent Detection", "#9467bd"),
            ("Slack Notification", "#8c564b"),
            ("Google Sheets", "#e377c2"),
            ("HubSpot CRM", "#7f7f7f")
        ]
        
        connections = [
            ("Web Form", "n8n Router"),
            ("Email Input", "n8n Router"),
            ("Webhook", "n8n Router"),
            ("n8n Router", "AI Intent Detection"),
            ("AI Intent Detection", "Slack Notification"),
            ("AI Intent Detection", "Google Sheets"),
            ("AI Intent Detection", "HubSpot CRM")
        ]
        
        fig = create_flowchart(nodes, connections, "Smart Lead Router Architecture")
        if PLOTLY_AVAILABLE:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.markdown(fig)
    
    st.markdown("### Lead Classification Matrix")
    
    # Sample lead classification data
    classification_data = pd.DataFrame({
        'Industry': ['Technology', 'Healthcare', 'Finance', 'Retail', 'Manufacturing'],
        'Qualified Leads': [145, 89, 123, 67, 92],
        'Conversion Rate': [23.4, 18.7, 29.1, 15.3, 21.8]
    })
    
    col1, col2 = st.columns(2)
    with col1:
        if PLOTLY_AVAILABLE:
            fig = go.Figure(data=[
                go.Bar(x=classification_data['Industry'], 
                       y=classification_data['Qualified Leads'],
                       marker_color='lightblue')
            ])
            fig.update_layout(title="Leads by Industry", height=300)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.subheader("Leads by Industry")
            st.bar_chart(classification_data.set_index('Industry')['Qualified Leads'])
    
    with col2:
        if PLOTLY_AVAILABLE:
            fig = go.Figure(data=[
                go.Bar(x=classification_data['Industry'], 
                       y=classification_data['Conversion Rate'],
                       marker_color='lightgreen')
            ])
            fig.update_layout(title="Conversion Rate by Industry (%)", height=300)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.subheader("Conversion Rate by Industry (%)")
            st.bar_chart(classification_data.set_index('Industry')['Conversion Rate'])

elif page == "3. OCR + Slack AI Bot":
    st.title("📄 OCR + Slack AI Bot")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        ### Project Overview
        Intelligent document processing system that extracts, analyzes, 
        and provides instant Q&A capabilities via Slack.
        
        ### Key Features
        - **Multi-format Support**: PDF, images, scanned documents
        - **Advanced OCR**: Tesseract + Google Vision API
        - **AI Summarization**: Context-aware document analysis
        - **Slack Integration**: Real-time Q&A bot
        
        ### Business Impact
        - **Processing Speed**
        - **Accuracy**
        - **Team Productivity**
        """)
    
    with col2:
        nodes = [
            ("Document Upload", "#1f77b4"),
            ("Streamlit UI", "#ff7f0e"),
            ("OCR Engine", "#2ca02c"),
            ("Text Extraction", "#d62728"),
            ("AI Summarizer", "#9467bd"),
            ("Slack Bot", "#8c564b"),
            ("Q&A Interface", "#e377c2")
        ]
        
        connections = [
            ("Document Upload", "Streamlit UI"),
            ("Streamlit UI", "OCR Engine"),
            ("OCR Engine", "Text Extraction"),
            ("Text Extraction", "AI Summarizer"),
            ("AI Summarizer", "Slack Bot"),
            ("Slack Bot", "Q&A Interface")
        ]
        
        fig = create_flowchart(nodes, connections, "OCR + Slack Bot Workflow")
        if PLOTLY_AVAILABLE:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.markdown(fig)
    
    # Document processing metrics
    st.markdown("### Processing Performance")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Documents Processed", "N/A", "↑ N/A")
    with col2:
        st.metric("Avg Processing Time", "N/A", "↓ N/A")
    with col3:
        st.metric("Slack Interactions", "N/A", "↑ N/A")

elif page == "4. AI Blog Writing Tool":
    st.title("AI Blog Writing Tool")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        ### Project Overview
        Automated content generation system that researches, writes, 
        and formats blog posts based on user specifications.
        
        ### Key Features
        - **AI Research**: Claude/Perplexity API integration
        - **Custom Training**: Upload writing samples
        - **Metadata Control**: Keywords, tone, audience targeting
        - **Multi-format Output**: HTML, Markdown, CMS-ready
        
        ### Business Impact
        - **Content Speed**: 10x faster blog creation
        - **Quality Consistency**
        - **Cost Reduction**
        """)
    
    with col2:
        nodes = [
            ("Topic Input", "#1f77b4"),
            ("AI Research", "#ff7f0e"),
            ("Training Samples", "#2ca02c"),
            ("Content Generator", "#d62728"),
            ("Metadata Engine", "#9467bd"),
            ("Streamlit UI", "#8c564b"),
            ("Export Options", "#e377c2"),
            ("CMS Integration", "#7f7f7f")
        ]
        
        connections = [
            ("Topic Input", "AI Research"),
            ("Training Samples", "Content Generator"),
            ("AI Research", "Content Generator"),
            ("Content Generator", "Metadata Engine"),
            ("Metadata Engine", "Streamlit UI"),
            ("Streamlit UI", "Export Options"),
            ("Export Options", "CMS Integration")
        ]
        
        fig = create_flowchart(nodes, connections, "AI Blog Writing Tool Pipeline")
        if PLOTLY_AVAILABLE:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.markdown(fig)
    
    st.markdown("### Content Generation Metrics")
    
    # Sample blog metrics
    blog_metrics = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Blogs Generated': [12, 18, 24, 31, 28, 35],
        'Avg Word Count': [1250, 1340, 1180, 1420, 1380, 1290]
    })
    
    col1, col2 = st.columns(2)
    with col1:
        if PLOTLY_AVAILABLE:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=blog_metrics['Month'], 
                                    y=blog_metrics['Blogs Generated'],
                                    mode='lines+markers',
                                    name='Blogs Generated',
                                    line=dict(color='blue', width=3)))
            fig.update_layout(title="Monthly Blog Generation", height=300)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.subheader("Monthly Blog Generation")
            st.line_chart(blog_metrics.set_index('Month')['Blogs Generated'])
    
    with col2:
        if PLOTLY_AVAILABLE:
            fig = go.Figure()
            fig.add_trace(go.Bar(x=blog_metrics['Month'], 
                                y=blog_metrics['Avg Word Count'],
                                marker_color='lightcoral'))
            fig.update_layout(title="Average Word Count", height=300)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.subheader("Average Word Count")
            st.bar_chart(blog_metrics.set_index('Month')['Avg Word Count'])

elif page == "5. Alibaba Lead Classifier":
    st.title("Alibaba Lead Classifier")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        ### Project Overview
        Automated B2B lead qualification system that scrapes and 
        analyzes Alibaba inquiries for business potential.
        
        ### Key Features
        - **Web Scraping**: Selenium/Playwright automation
        - **Data Extraction**: Sender info, previews, timestamps
        - **AI Classification**: LLaMA/OpenAI intent analysis
        - **Lead Storage**: Google Sheets integration
        
        ### Business Impact
        - **Lead Volume**: 245% increase in qualified leads
        - **Processing Speed**
        - **Accuracy**
        """)
    
    with col2:
        nodes = [
            ("Alibaba Platform", "#1f77b4"),
            ("Web Scraper", "#ff7f0e"),
            ("Data Extraction", "#2ca02c"),
            ("LLM Classifier", "#d62728"),
            ("Intent Analysis", "#9467bd"),
            ("Lead Scoring", "#8c564b"),
            ("Google Sheets", "#e377c2")
        ]
        
        connections = [
            ("Alibaba Platform", "Web Scraper"),
            ("Web Scraper", "Data Extraction"),
            ("Data Extraction", "LLM Classifier"),
            ("LLM Classifier", "Intent Analysis"),
            ("Intent Analysis", "Lead Scoring"),
            ("Lead Scoring", "Google Sheets")
        ]
        
        fig = create_flowchart(nodes, connections, "Alibaba Lead Classifier System")
        if PLOTLY_AVAILABLE:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.markdown(fig)
    
    st.markdown("### Geographic Lead Distribution")
    
    # Sample geographic data
    geo_data = pd.DataFrame({
        'Region': ['Asia-Pacific', 'Europe', 'North America'],
        'Lead Count': [342, 156, 89],
        'Quality Score': [8.2, 7.8, 9.1]
    })
    
    if PLOTLY_AVAILABLE:
        col1, col2 = st.columns(2)
        with col1:
            fig = go.Figure(data=[go.Pie(labels=geo_data['Region'], 
                                        values=geo_data['Lead Count'],
                                        hole=.3)])
            fig.update_layout(title="Leads by Region", height=300)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=geo_data['Region'], 
                                    y=geo_data['Quality Score'],
                                    mode='markers',
                                    marker=dict(size=geo_data['Lead Count'], 
                                              sizemode='area',
                                              sizeref=2.*max(geo_data['Lead Count'])/(40.**2),
                                              sizemin=4)))
            fig.update_layout(title="Quality Score by Region", height=300)
            st.plotly_chart(fig, use_container_width=True)
    else:
        # Fallback: Display data in columns
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Leads by Region")
            for _, row in geo_data.iterrows():
                st.write(f"**{row['Region']}**: {row['Lead Count']} leads")
        
        with col2:
            st.subheader("Quality Scores")
            for _, row in geo_data.iterrows():
                st.write(f"**{row['Region']}**: {row['Quality Score']}/10")

elif page == "6. Outlook Email Classifier":
    st.title("Outlook Email Classifier")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        ### Project Overview
        Microsoft Outlook integration that analyzes email threads 
        for lead qualification using advanced context understanding.
        
        ### Key Features
        - **Microsoft Graph API**: Secure Outlook integration
        - **Thread Analysis**: Context-aware classification
        - **Streamlit Interface**: Interactive result management
        - **Smart Storage**: Google Sheets with thread tracking
        
        ### Business Impact
        - **Email Processing**
        - **Thread Accuracy**
        - **Response Time**
        """)
    
    with col2:
        nodes = [
            ("Outlook Email", "#1f77b4"),
            ("Graph API", "#ff7f0e"),
            ("Email Threads", "#2ca02c"),
            ("Context Analysis", "#d62728"),
            ("LLM Classifier", "#9467bd"),
            ("Streamlit Dashboard", "#8c564b"),
            ("Google Sheets", "#e377c2")
        ]
        
        connections = [
            ("Outlook Email", "Graph API"),
            ("Graph API", "Email Threads"),
            ("Email Threads", "Context Analysis"),
            ("Context Analysis", "LLM Classifier"),
            ("LLM Classifier", "Streamlit Dashboard"),
            ("Streamlit Dashboard", "Google Sheets")
        ]
        
        fig = create_flowchart(nodes, connections, "Outlook Email Classifier Flow")
        if PLOTLY_AVAILABLE:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.markdown(fig)
    
    st.markdown("### Email Classification Performance")
    
    # Performance metrics over time
    dates = pd.date_range(start='2024-01-01', periods=6, freq='M')
    performance_data = pd.DataFrame({
        'Month': dates.strftime('%b'),
        'Emails Processed': [450, 520, 680, 750, 820, 890],
        'Leads Identified': [67, 78, 102, 115, 124, 135],
        'Accuracy %': [89.2, 91.5, 92.8, 93.1, 93.7, 94.2]
    })
    
    col1, col2 = st.columns(2)
    with col1:
        if PLOTLY_AVAILABLE:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=performance_data['Month'], 
                                    y=performance_data['Emails Processed'],
                                    mode='lines+markers',
                                    name='Emails Processed',
                                    line=dict(color='blue')))
            fig.add_trace(go.Scatter(x=performance_data['Month'], 
                                    y=performance_data['Leads Identified'],
                                    mode='lines+markers',
                                    name='Leads Identified',
                                    line=dict(color='green')))
            fig.update_layout(title="Processing Volume Trends", height=300)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.subheader("Processing Volume Trends")
            chart_data = performance_data.set_index('Month')[['Emails Processed', 'Leads Identified']]
            st.line_chart(chart_data)
    
    with col2:
        if PLOTLY_AVAILABLE:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=performance_data['Month'], 
                                    y=performance_data['Accuracy %'],
                                    mode='lines+markers',
                                    fill='tonexty',
                                    line=dict(color='orange')))
            fig.update_layout(title="Classification Accuracy Trend", height=300)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.subheader("Classification Accuracy Trend")
            st.line_chart(performance_data.set_index('Month')['Accuracy %'])

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.9rem; margin-top: 2rem;'>
    <p>AI Automation Portfolio Dashboard | Built with Streamlit & Python</p>
    <p>🤖 Empowering Business Through Intelligent Automation</p>
</div>
""", unsafe_allow_html=True)
