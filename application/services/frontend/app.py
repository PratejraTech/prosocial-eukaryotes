import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Page config
st.set_page_config(
    page_title="PILAR Research Platform",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
.metric-card {
    background-color: #f0f2f6;
    padding: 1rem;
    border-radius: 0.5rem;
    border-left: 4px solid #1f77b4;
}
.hypothesis-card {
    background-color: #fff3cd;
    padding: 1rem;
    border-radius: 0.5rem;
    border-left: 4px solid #ffc107;
}
</style>
""", unsafe_allow_html=True)

def main():
    st.title("🧠 PILAR Research Platform")
    st.markdown("*Prosocial Behavior and Collaboration Dynamics Research*")
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select Page", [
        "Overview", 
        "PILAR Assessment", 
        "Hypothesis Testing", 
        "Case Studies", 
        "Research Database"
    ])
    
    if page == "Overview":
        show_overview()
    elif page == "PILAR Assessment":
        show_pilar_assessment()
    elif page == "Hypothesis Testing":
        show_hypothesis_testing()
    elif page == "Case Studies":
        show_case_studies()
    elif page == "Research Database":
        show_research_database()

def show_overview():
    st.header("Project Overview")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### PILAR Model Framework
        The **PILAR** model (Prospects, Involved, Liked, Agency, Respect) encapsulates over 30 social and group psychology theories to assess collaboration viability in complex environments.
        
        **Core Components:**
        - **Prospects**: Likelihood of achieving group goals
        - **Involved**: Mutual cooperation and assistance
        - **Liked**: Belonging and popularity within collaboration
        - **Agency**: Ability to suggest strategic changes
        - **Respect**: Trust in colleagues' knowledge, skills, and abilities
        """)
        
        # PILAR Forces Visualization
        st.subheader("PILAR Force Network")
        fig = create_pilar_network()
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("SGP Theories", "30+", "Integrated")
        st.metric("Causal Forces", "20", "14 positive, 6 negative")
        st.metric("Research Papers", "50+", "Analyzed")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.subheader("Key Hypotheses")
        hypotheses = [
            "H1: PILAR training increases prosocial orientation",
            "H2: Inequality aversion predicts prosocial engagement", 
            "H3: Egalitarian structures boost trio feedback",
            "H4: Low prosociality causes learning reticence",
            "H5: Hierarchy balances confidence vs. trio health"
        ]
        for h in hypotheses:
            st.markdown(f"- {h}")

def show_pilar_assessment():
    st.header("PILAR Collaboration Assessment")
    
    st.markdown("""
    ### Interactive PILAR Evaluation
    Rate each pillar on a scale of 1-10 based on your current collaboration context.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Pillar Ratings")
        prospects = st.slider("Prospects", 1, 10, 5, help="Likelihood of achieving group goals")
        involved = st.slider("Involved", 1, 10, 5, help="Level of mutual cooperation")
        liked = st.slider("Liked", 1, 10, 5, help="Sense of belonging and popularity")
        agency = st.slider("Agency", 1, 10, 5, help="Ability to suggest changes")
        respect = st.slider("Respect", 1, 10, 5, help="Trust in colleagues' abilities")
        
        # Calculate viability score
        viability = np.mean([prospects, involved, liked, agency, respect])
        
        if viability >= 7:
            status = "High Viability"
            color = "green"
        elif viability >= 5:
            status = "Moderate Viability"
            color = "orange"
        else:
            status = "Low Viability"
            color = "red"
            
        st.markdown(f"**Collaboration Viability: <span style='color:{color}'>{status}</span>** ({viability:.1f}/10)", unsafe_allow_html=True)
    
    with col2:
        # PILAR radar chart
        fig = create_pilar_radar([prospects, involved, liked, agency, respect])
        st.plotly_chart(fig, use_container_width=True)
        
        # Force analysis
        st.subheader("Force Analysis")
        forces = analyze_forces(prospects, involved, liked, agency, respect)
        for force, strength in forces.items():
            if strength > 0:
                st.success(f"✓ {force}: Strong positive force")
            else:
                st.warning(f"⚠ {force}: Potential negative force")

def show_hypothesis_testing():
    st.header("Hypothesis Testing Framework")
    
    tab1, tab2, tab3 = st.tabs(["Hypothesis Overview", "Simulation", "Results"])
    
    with tab1:
        st.subheader("Research Hypotheses")
        
        hypotheses_data = {
            "H1": {
                "title": "PILAR Training Effect",
                "description": "Teaching PILAR/EUCRM increases prosocial orientation and group viability, mediated by pillar awareness; stronger in low-empathy individuals.",
                "test": "RCT with SCARF comparison, measure CA via peer-assessment"
            },
            "H2": {
                "title": "Inequality Aversion Impact", 
                "description": "High inequality aversion predicts elevated Respect/Involved perceptions and prosocial engagement, moderating zero-sum avoidance.",
                "test": "Primate-inspired ultimatum games in teams; correlate with sGLS proxies"
            },
            "H3": {
                "title": "Egalitarian Structure Effects",
                "description": "Egalitarian structures boost liking/respect/communication but reduce agency/confidence, leading to stable yet less adaptive groups.",
                "test": "Simulate dimorphism in Pan/hominin models; organizational case studies"
            }
        }
        
        for h_id, h_data in hypotheses_data.items():
            with st.expander(f"{h_id}: {h_data['title']}"):
                st.markdown(f"**Description:** {h_data['description']}")
                st.markdown(f"**Test Method:** {h_data['test']}")
    
    with tab2:
        st.subheader("PILAR Force Simulation")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Simulation Parameters**")
            n_agents = st.slider("Number of Agents", 5, 50, 20)
            hierarchy_level = st.slider("Hierarchy Level", 0.0, 1.0, 0.3)
            inequality_aversion = st.slider("Inequality Aversion", 0.0, 1.0, 0.7)
            
            if st.button("Run Simulation"):
                results = run_pilar_simulation(n_agents, hierarchy_level, inequality_aversion)
                st.session_state.sim_results = results
        
        with col2:
            if 'sim_results' in st.session_state:
                fig = plot_simulation_results(st.session_state.sim_results)
                st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.subheader("Research Findings")
        st.markdown("""
        ### Key Findings from Literature Analysis
        
        **Prosocial Evolution:**
        - Inequality aversion, interdependence, and tolerance facilitate prosocial behaviors
        - Sub-group level selection (sGLS) explains human divergence from Pan ancestors
        
        **Collaboration Dynamics:**
        - Positive-sum behaviors build collaborative ability through trust-based relationships
        - Zero-sum actions (free-riding, credit-seeking) undermine collaboration
        
        **Cultural Transformation:**
        - Shift from domination to partnership systems via egalitarian structures
        - PILAR model provides micro-level intervention framework
        """)

def show_case_studies():
    st.header("Case Studies in Complex Environments")
    
    case_studies = {
        "Primate Troops in Savannah": {
            "context": "Behavioral dimorphism in Pan under savannah pressures",
            "complexity": "Evolutionary adaptation and resource scarcity",
            "pilar_dynamics": "Low Prospects → Agency innovation; egalitarian shifts boost Involved/Liked",
            "outcome": "Hominin divergence with unique coordination/compassion capabilities"
        },
        "Healthcare Research Teams": {
            "context": "Interdisciplinary teams in Mothers and Babies Research Centre",
            "complexity": "Hierarchy vs. innovation tensions",
            "pilar_dynamics": "Steep hierarchy → high confidence/performance but low respect",
            "outcome": "Improved CA through flattened hierarchies and equity focus"
        },
        "Online Learning Platforms": {
            "context": "Self-learners engaging with prosocial content",
            "complexity": "Unpredictable engagement and zero-sum reticence",
            "pilar_dynamics": "Low QoL predicts early disengagement; ancestral norm priming helps",
            "outcome": "Higher engagement through targeted interventions"
        }
    }
    
    selected_case = st.selectbox("Select Case Study", list(case_studies.keys()))
    
    case = case_studies[selected_case]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Case Context")
        st.markdown(f"**Environment:** {case['context']}")
        st.markdown(f"**Complexity Factors:** {case['complexity']}")
        
        st.subheader("PILAR Dynamics")
        st.markdown(case['pilar_dynamics'])
    
    with col2:
        st.subheader("Outcomes")
        st.markdown(case['outcome'])
        
        # Simulate case study data
        fig = create_case_study_visualization(selected_case)
        st.plotly_chart(fig, use_container_width=True)

def show_research_database():
    st.header("Research Database")
    
    tab1, tab2, tab3 = st.tabs(["Documents", "Researchers", "Theories"])
    
    with tab1:
        st.subheader("Research Documents")
        
        # Mock document database
        docs = pd.DataFrame({
            'Title': [
                'Prosocial behaviors in nonhuman animals',
                'Sub-group level selection in hominins', 
                'PILAR Model Development',
                'Cultural Transformation Theory',
                'Inequality Aversion in Primates'
            ],
            'Type': ['Abstract', 'Abstract', 'Model', 'Theory', 'Research'],
            'Year': [2020, 2021, 2019, 2018, 2019],
            'Citations': [45, 23, 12, 67, 34],
            'Relevance': ['High', 'High', 'Critical', 'Medium', 'High']
        })
        
        st.dataframe(docs, use_container_width=True)
    
    with tab2:
        st.subheader("Key Researchers")
        
        researchers = {
            "19th Century": ["Darwin (moral instincts)", "Kropotkin (mutual aid)"],
            "20th Century": ["Lewin (field theory)", "Moreno (sociometry)", "de Waal (primate behavior)", "Axelrod (cooperation evolution)"],
            "Contemporary": ["Heslop (PILAR model)", "Boehm (reverse dominance)", "Trivers (reciprocal altruism)"]
        }
        
        for period, names in researchers.items():
            st.markdown(f"**{period}:**")
            for name in names:
                st.markdown(f"- {name}")
    
    with tab3:
        st.subheader("Integrated Theories")
        
        theories = pd.DataFrame({
            'Theory': [
                'Social Identity Theory',
                'Social Network Analysis', 
                'Psychological Safety',
                'Cultural Transformation Theory',
                'Human Possibilities Theory'
            ],
            'PILAR Integration': [
                'Liked → Involved dynamics',
                'Respect → Network centrality',
                'Agency → Change suggestions',
                'Macro-level partnership systems',
                'Egalitarian behavior promotion'
            ],
            'Evidence Level': ['Strong', 'Strong', 'Moderate', 'Emerging', 'Theoretical']
        })
        
        st.dataframe(theories, use_container_width=True)

def create_pilar_network():
    """Create network visualization of PILAR forces"""
    fig = go.Figure()
    
    # Node positions (pentagon)
    angles = np.linspace(0, 2*np.pi, 6)[:-1]
    x = np.cos(angles)
    y = np.sin(angles)
    
    labels = ['Prospects', 'Involved', 'Liked', 'Agency', 'Respect']
    
    # Add nodes
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='markers+text',
        marker=dict(size=50, color='lightblue'),
        text=labels,
        textposition="middle center",
        name="PILAR Pillars"
    ))
    
    # Add force connections (simplified)
    for i in range(5):
        for j in range(5):
            if i != j:
                fig.add_trace(go.Scatter(
                    x=[x[i], x[j]], y=[y[i], y[j]],
                    mode='lines',
                    line=dict(width=1, color='gray'),
                    showlegend=False,
                    opacity=0.3
                ))
    
    fig.update_layout(
        title="PILAR Force Network",
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        height=400
    )
    
    return fig

def create_pilar_radar(values):
    """Create radar chart for PILAR assessment"""
    categories = ['Prospects', 'Involved', 'Liked', 'Agency', 'Respect']
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]],  # Close the polygon
        theta=categories + [categories[0]],
        fill='toself',
        name='Current Assessment'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )),
        showlegend=False,
        title="PILAR Assessment Radar"
    )
    
    return fig

def analyze_forces(prospects, involved, liked, agency, respect):
    """Analyze PILAR forces based on current values"""
    forces = {}
    
    # Positive forces (simplified analysis)
    if involved > 6 and liked > 6:
        forces["Involved → Liked"] = 1
    else:
        forces["Involved → Liked"] = -1
        
    if agency > 6 and prospects > 6:
        forces["Agency → Prospects"] = 1
    else:
        forces["Agency → Prospects"] = -1
        
    if respect > 6 and involved > 6:
        forces["Respect → Involved"] = 1
    else:
        forces["Respect → Involved"] = -1
    
    return forces

def run_pilar_simulation(n_agents, hierarchy, inequality_aversion):
    """Run simplified PILAR simulation"""
    np.random.seed(42)
    
    # Generate agent data
    agents = pd.DataFrame({
        'agent_id': range(n_agents),
        'prospects': np.random.normal(5 + hierarchy, 2, n_agents),
        'involved': np.random.normal(6 - hierarchy*2, 1.5, n_agents),
        'liked': np.random.normal(5 + inequality_aversion, 1.5, n_agents),
        'agency': np.random.normal(6 - hierarchy*3, 2, n_agents),
        'respect': np.random.normal(5 + inequality_aversion*2, 1.5, n_agents)
    })
    
    # Clip values to 1-10 range
    for col in ['prospects', 'involved', 'liked', 'agency', 'respect']:
        agents[col] = np.clip(agents[col], 1, 10)
    
    return agents

def plot_simulation_results(results):
    """Plot simulation results"""
    fig = make_subplots(
        rows=2, cols=3,
        subplot_titles=['Prospects', 'Involved', 'Liked', 'Agency', 'Respect', 'Overall'],
        specs=[[{"type": "histogram"}, {"type": "histogram"}, {"type": "histogram"}],
               [{"type": "histogram"}, {"type": "histogram"}, {"type": "scatter"}]]
    )
    
    pillars = ['prospects', 'involved', 'liked', 'agency', 'respect']
    
    for i, pillar in enumerate(pillars):
        row = (i // 3) + 1
        col = (i % 3) + 1
        
        fig.add_trace(
            go.Histogram(x=results[pillar], name=pillar.title()),
            row=row, col=col
        )
    
    # Overall viability scatter
    results['viability'] = results[pillars].mean(axis=1)
    fig.add_trace(
        go.Scatter(
            x=results.index, 
            y=results['viability'],
            mode='markers',
            name='Viability'
        ),
        row=2, col=3
    )
    
    fig.update_layout(height=600, showlegend=False, title="Simulation Results")
    return fig

def create_case_study_visualization(case_name):
    """Create visualization for case study"""
    # Mock time series data for case study
    time = np.arange(0, 100, 1)
    
    if case_name == "Primate Troops in Savannah":
        prospects = 3 + 2 * np.sin(time/20) + np.random.normal(0, 0.5, len(time))
        agency = 4 + 3 * np.cos(time/15) + np.random.normal(0, 0.3, len(time))
    elif case_name == "Healthcare Research Teams":
        prospects = 6 + np.random.normal(0, 1, len(time))
        agency = 3 + 2 * (time/100) + np.random.normal(0, 0.5, len(time))
    else:  # Online Learning
        prospects = 5 + np.random.normal(0, 0.8, len(time))
        agency = 4 + 1.5 * np.tanh((time-50)/20) + np.random.normal(0, 0.4, len(time))
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time, y=prospects, name='Prospects', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=time, y=agency, name='Agency', line=dict(color='red')))
    
    fig.update_layout(
        title=f"PILAR Dynamics: {case_name}",
        xaxis_title="Time",
        yaxis_title="Pillar Strength",
        height=400
    )
    
    return fig

if __name__ == "__main__":
    main()