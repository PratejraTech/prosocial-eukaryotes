import json
import uuid
from datetime import datetime

# Core themes and hypotheses
core_themes = [
    "PILAR model (Prospects, Involved, Liked, Agency, Respect)",
    "Prosocial evolution and sub-group level selection (sGLS)",
    "Inequality aversion in collaboration",
    "Thorngate’s Postulate of Commensurate Complexity",
    "Deep Research Agent (DRA) for practical application",
    "Egalitarian behavior and cultural transformation",
    "Positive-sum vs. zero-sum dynamics"
]
hypotheses = [
    "Teaching PILAR/EUCRM increases prosocial orientation and group viability, mediated by pillar awareness, especially in low-empathy individuals.",
    "High inequality aversion predicts elevated Respect/Involved perceptions and prosocial engagement, moderating zero-sum avoidance.",
    "Egalitarian structures boost liking/respect/communication but reduce agency/confidence, affecting adaptability in resource-scarce ecologies.",
    "Low prosociality (low QoL/EQ) causes reticence in prosocial learning, requiring ancestral norm priming for engagement.",
    "Hierarchy steepness balances confidence/performance vs. trio (health), optimal in actualization hierarchies."
]
theories = [
    "Social Identity Theory (SIT)",
    "Social Network Analysis (SNA)",
    "Psychological Safety",
    "Field Theory (Lewin)",
    "Cognitive Dissonance (Festinger)",
    "Inequity Aversion (de Waal)"
]
sources = [
    "hypothesese2.md", "technology-collaboration.md", "hypothese1.md",
    "abstract.md", "A-Model-Of-Collaboration.pdf"
]

# Function to generate Q&A pairs with authors' style
def generate_qa_pairs():
    qa_pairs = []
    timestamp = "2025-10-20T12:13:00Z"  # 11:13 PM ACDT = 12:13 PM UTC

    for i in range(3000):
        # Generate unique question ID and base structure
        q_id = f"Q{i+1}"
        theme = core_themes[i % len(core_themes)]
        hypo = hypotheses[i % len(hypotheses)]
        theory = theories[i % len(theories)]
        source = sources[i % len(sources)]

        # Construct question with scholarly tone and hypothesis focus
        question_types = [
            f"How might {theme} enhance collaboration viability in light of {hypo}?",
            f"What role does {theory} play in validating {hypo} within {theme}?",
            f"Can {theme} address the challenge posed by {hypo}, drawing on {theory}?",
            f"To what extent does {hypo} influence the efficacy of {theme}, per {theory}?"
        ]
        question = f"{q_id}: {question_types[i % len(question_types)]}"

        # Construct answer with authors' optimistic yet cautious style
        answer_base = {
            "PILAR model": "The PILAR model, with its five pillars and 20 interlinked forces, offers a promising synthesis of over 30 SGP theories, potentially enhancing collaboration viability if applied through idealized conditions.",
            "Prosocial evolution and sGLS": "Prosocial evolution, driven by sGLS, suggests an exponential advantage in hominin collaboration, rooted in savannah ecology, though empirical validation remains a future endeavor.",
            "Inequality aversion in collaboration": "Inequality aversion, a cornerstone of prosociality, punishes unfairness and fosters Respect, yet its impact may wane in hierarchical settings unless mitigated by DRA.",
            "Thorngate’s Postulate": "Thorngate’s Postulate highlights the trade-off between generality, accuracy, and simplicity in PILAR, necessitating AI agents like DRA to bridge this complexity gap.",
            "Deep Research Agent (DRA)": "The DRA, powered by LLMs, acts as an empathetic coach, translating PILAR’s complexity into actionable guidance, though its efficacy hinges on bias mitigation.",
            "Egalitarian behavior and cultural transformation": "Egalitarian behavior stabilizes groups via the communication-respect-liking trio, yet may stifle Agency, a tension we believe can be balanced with careful design.",
            "Positive-sum vs. zero-sum dynamics": "Positive-sum dynamics build CA through trust, countering zero-sum reticence, a challenge we see as addressable with ancestral norm priming."
        }
        theory_insight = {
            "Social Identity Theory (SIT)": "SIT underscores how Liked perceptions shape ingroup cohesion, aligning with PILAR’s evolutionary adaptive mechanisms.",
            "Social Network Analysis (SNA)": "SNA reveals network centrality’s role in Involved perceptions, supporting PILAR’s force dynamics.",
            "Psychological Safety": "Psychological safety fosters Agency, a pillar we deem critical for innovation within PILAR.",
            "Field Theory (Lewin)": "Lewin’s field theory informs Prospects as a function of social forces, a concept we integrate into PILAR’s structure.",
            "Cognitive Dissonance (Festinger)": "Festinger’s dissonance explains Agency’s impact on Liked, a nuance we explore for collaboration resistance.",
            "Inequity Aversion (de Waal)": "de Waal’s inequity aversion links to Respect, reinforcing PILAR’s prosocial foundation."
        }
        answer = f"{answer_base[theme]} We contend that {theory_insight[theory]} offers a robust lens, though further empirical testing is prudent to affirm these insights."

        qa_pairs.append({
            "question": question,
            "answer": answer,
            "source": source,
            "timestamp": timestamp
        })

    return qa_pairs

# Generate and write to .jsonl file
qa_data = generate_qa_pairs()
with open("synthetic_qa_phi4.jsonl", "w", encoding="utf-8") as f:
    for item in qa_data:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print("File 'synthetic_qa_phi4.jsonl' has been created with 3000 Q&A pairs.")