# Data Outputs: Use Cases and Applications

This directory contains synthetic Q&A pairs and methodological documentation for PILAR/EUCRM collaboration research. The data serves dual purposes: traditional empirical research validation and novel AI-augmented research methodologies.

---

## Traditional Research Applications (Technical)

### Quantitative Analysis Frameworks
#### Note: The below assumes rigorous testing of methodology of generating pairs.

#### It should also be noted that more complex schemas and steering of the models are possible whne using appropriate context or prompt engineering.

**1. Hypothesis Testing via Content Analysis**

The 2,500+ Q&A pairs provide a structured corpus for validating the five core hypotheses (H1-H5) through:

- **Thematic Coding**: Apply NVivo or ATLAS.ti to code responses by pillar (Prospects, Involved, Liked, Agency, Respect), theory (SIT, SNA, etc.), and hypothesis alignment. Calculate inter-rater reliability (Cohen's κ > 0.80) to ensure coding consistency.

- **Frequency Distribution Analysis**: Use chi-square tests to assess whether theme-hypothesis pairings deviate from expected uniform distribution, revealing potential theoretical biases or gaps in the synthetic generation logic.

- **Semantic Network Analysis**: Employ Gephi or NetworkX to construct co-occurrence networks of concepts (e.g., "inequality aversion" ↔ "Respect pillar"). Centrality metrics (betweenness, eigenvector) identify theoretical linchpins within the PILAR framework.

**2. Psychometric Validation**

- **Construct Validity**: Extract latent dimensions via exploratory factor analysis (EFA) on question-answer semantic embeddings (e.g., BERT, sentence-transformers). Confirm whether factors align with the seven core themes or reveal emergent constructs.

- **Convergent/Discriminant Validity**: Correlate synthetic data patterns with established scales (e.g., Prosocial Behavioral Intentions Scale, Empathy Quotient) using Spearman's ρ. High convergence (ρ > 0.60) with prosocial measures validates thematic coherence.

**3. Longitudinal Simulation Studies**

- **Agent-Based Modeling (ABM)**: Integrate Q&A pairs as knowledge bases for simulated agents in Mesa or NetLogo. Model collaboration dynamics under varying hierarchy steepness (H5) or inequality aversion levels (H2). Track emergent viability metrics (e.g., group cohesion indices) over 1,000+ iterations.

- **Time-Series Forecasting**: If paired with temporal metadata (e.g., pre/post PILAR training), apply ARIMA or LSTM models to predict prosocial orientation shifts, testing H1's mediation hypothesis.

**4. Meta-Analytic Integration**

- **Effect Size Extraction**: Parse answers for implicit effect sizes (e.g., "exponential advantage" → Cohen's d estimation). Aggregate across themes using random-effects models (Hedges' g) to synthesize PILAR's purported impact.

- **Moderator Analysis**: Test whether theory type (SIT vs. SNA) or abstraction level (strategic vs. tactical) moderates question-answer coherence, using meta-regression with restricted maximum likelihood (REML).

### Qualitative Research Pathways

**1. Grounded Theory Development**

- **Open Coding**: Identify in-vivo codes (e.g., "trio feedback loop," "zero-sum reticence") from answers. Use constant comparison to refine categories until theoretical saturation.

- **Axial Coding**: Map relationships between categories (e.g., egalitarian structures → reduced Agency → innovation stifling), constructing a process model of collaboration viability.

**2. Discourse Analysis**

- **Critical Discourse Analysis (CDA)**: Examine how answers position PILAR as "promising yet cautious," revealing ideological commitments to empirical rigor vs. theoretical optimism. Analyze modal verbs ("may," "can," "must") to assess epistemic certainty.

- **Rhetorical Structure Theory (RST)**: Parse answer argumentation patterns (claim → evidence → warrant). Quantify reliance on evolutionary vs. psychological evidence bases.

### Data Preparation for Statistical Software

**Export Formats:**
- **R/Python**: Convert JSONL to data frames with columns: `question_id`, `theme`, `hypothesis`, `theory`, `source`, `answer_length`, `sentiment_score` (via VADER/TextBlob).
- **SPSS/Stata**: Generate CSV with categorical variables (theme, theory) and continuous variables (answer complexity via Flesch-Kincaid).
- **MAXQDA**: Import as text corpus with metadata tags for mixed-methods triangulation.

**Preprocessing Pipeline:**
```python
import pandas as pd
import json

# Load JSONL
data = [json.loads(line) for line in open('synthetic_qa_phi4.jsonl')]
df = pd.DataFrame(data)

# Feature engineering
df['answer_length'] = df['answer'].str.len()
df['theme'] = df['question'].str.extract(r'(PILAR model|Prosocial evolution|Inequality aversion|Thorngate|DRA|Egalitarian|Positive-sum)')
df['hypothesis'] = df['question'].str.extract(r'(Teaching PILAR|High inequality aversion|Egalitarian structures|Low prosociality|Hierarchy steepness)')

# Export for analysis
df.to_csv('qa_analysis_ready.csv', index=False)
```

---

## AI-Augmented Research: Small Language Model Training

### Specialized Model Development

**Objective**: Fine-tune a domain-specific small language model (SLM) on PILAR/EUCRM research to create an expert system for collaboration analysis.

**1. Model Selection & Architecture**

- **Base Models**: Microsoft Phi-4 (14B parameters), Mistral-7B, or Llama-3-8B provide optimal balance between specialization capacity and computational efficiency.

- **Fine-Tuning Framework**: Use Unsloth for memory-efficient training with QLoRA (4-bit quantization + Low-Rank Adaptation). Target layers: attention heads (Q, K, V matrices) and feed-forward networks.

**2. Training Configuration**

```python
from unsloth import FastLanguageModel
import torch

# Load base model
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="microsoft/phi-4",
    max_seq_length=2048,
    dtype=torch.float16,
    load_in_4bit=True
)

# Configure LoRA
model = FastLanguageModel.get_peft_model(
    model,
    r=16,  # Rank
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
    lora_alpha=16,
    lora_dropout=0.05,
    bias="none"
)

# Training hyperparameters
from transformers import TrainingArguments

training_args = TrainingArguments(
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    warmup_steps=50,
    max_steps=500,  # Adjust based on dataset size
    learning_rate=2e-4,
    fp16=True,
    logging_steps=10,
    output_dir="pilar_specialist_model"
)
```

**3. Evaluation Metrics**

- **Perplexity**: Target < 15 on held-out test set (20% of Q&A pairs)
- **BLEU Score**: Measure answer generation fidelity (target > 0.40)
- **Semantic Similarity**: Cosine similarity between generated and ground-truth answers using sentence embeddings (target > 0.75)

### Model Capabilities Post-Training

The specialized SLM will:
- **Answer domain-specific queries** with PILAR-grounded responses
- **Generate hypothesis-driven research questions** for empirical studies
- **Critique collaboration scenarios** through the lens of the five pillars
- **Suggest interventions** based on force dynamics (e.g., "boost communication to counter low Respect")

---

## Symmetrical Intelligence Augmentation (SIA)

**Concept Origin**: A. Moir, 2023

### What is Symmetrical Intelligence Augmentation?

Think of it as a two-way learning partnership between humans and AI, where both sides get smarter together—like a study group where everyone teaches and learns at the same time.

**The Traditional Approach (One-Way)**:
- Humans create data → AI learns from it → AI helps humans
- Problem: AI only knows what we explicitly teach it

**Symmetrical Intelligence Augmentation (Two-Way)**:
- Humans create seed data (our Q&A pairs) → Small AI learns deeply about one topic
- Small AI generates new variations → Big AI (like GPT-4) reviews and expands them
- Humans study the expanded data → Discover new patterns we didn't see before
- New insights feed back into better questions → The cycle continues

### How It Works in Practice

**Step 1: Train the Specialist (Small Model)**
- Our 2,500 Q&A pairs teach a small AI to become a PILAR collaboration expert
- Like training a research assistant who knows this one topic inside-out

**Step 2: Generate Variations (Small Model + Big Model)**
- The specialist AI creates 10,000 new questions about collaboration
- A big AI (foundation model) checks them for quality and adds depth
- Both AIs working together create more diverse, nuanced content than either alone

**Step 3: Human Discovery (Researchers)**
- Researchers read through the expanded dataset
- Find unexpected connections (e.g., "Wait, inequality aversion affects team innovation in ways we hadn't considered!")
- These discoveries become new research questions

**Step 4: Feedback Loop (The "Symmetrical" Part)**
- New research questions go back into the training data
- Both the small specialist and big generalist AIs learn from human insights
- Humans learn from AI-generated patterns
- **Everyone gets smarter together**

### Why "Symmetrical"?

Traditional AI: Humans → AI (one direction)

Symmetrical AI: Humans ⇄ Small AI ⇄ Big AI (all directions)

The intelligence flows in a circle, with each participant contributing unique strengths:
- **Humans**: Deep understanding, creativity, real-world context
- **Small AI**: Focused expertise, pattern consistency, rapid variation generation
- **Big AI**: Broad knowledge, quality control, cross-domain connections

### Real-World Example

**Without SIA**:
Researcher thinks: "I wonder if egalitarian teams are less innovative?"
→ Designs study → Collects data → Analyzes → Publishes (2-3 years)

**With SIA**:
1. Researcher asks specialist AI: "Generate 100 scenarios about egalitarian teams and innovation"
2. Specialist AI creates scenarios based on PILAR principles
3. Big AI expands each scenario with cross-disciplinary insights (psychology + economics + anthropology)
4. Researcher spots pattern: "Agency reduction happens specifically in resource-scarce contexts!"
5. This insight refines the specialist AI's understanding
6. New, more targeted scenarios emerge
7. Research accelerates from years to months

### Benefits for Non-Experts

- **Faster Learning**: The AI explains complex collaboration theories in multiple ways until you understand
- **Personalized Exploration**: Ask "what if" questions and get instant, research-grounded answers
- **Pattern Recognition**: The AI spots connections across thousands of examples that would take humans months to find
- **Continuous Improvement**: As more people use the system, it gets better at explaining and discovering

### The Future Vision

Imagine a research ecosystem where:
- Graduate students use specialist AIs as tireless research partners
- Foundation models connect insights across all of science
- Human researchers focus on creative hypothesis generation and real-world application
- The boundary between "human insight" and "AI insight" blurs into collaborative discovery

This is Symmetrical Intelligence Augmentation: not replacing human intelligence, but creating a dance where human creativity and AI processing power amplify each other in an endless cycle of mutual learning.

---

## File Inventory

### Core Data Files

**`synthetic_qa_phi4.jsonl`** (2,500-3,000 entries)
- Format: JSON Lines (one object per line)
- Schema: `{question, answer, source, timestamp}`
- Size: ~5-8 MB
- Use: Direct input for LLM fine-tuning or statistical analysis

**`qa-pairs-gen.py`**
- Purpose: Seed data generator with modulo-based cycling
- Customization: Modify `core_themes`, `hypotheses`, `theories` lists to adjust output
- Extensibility: Add style variations or abstraction levels for richer datasets

**`APPROACH.md`**
- Content: Methodological rationale, hypothesis definitions, BMAD framework
- Audience: Researchers seeking theoretical grounding for data generation logic

### Recommended Workflow

**For Empirical Researchers:**
1. Import `synthetic_qa_phi4.jsonl` into analysis software
2. Conduct exploratory data analysis (EDA) to identify theme distributions
3. Apply statistical tests aligned with research questions (see "Quantitative Analysis Frameworks" above)
4. Cross-validate findings with primary data from field studies or experiments

**For AI/ML Practitioners:**
1. Split data: 80% train, 10% validation, 10% test
2. Fine-tune SLM using Unsloth or Hugging Face Transformers
3. Evaluate on held-out test set with perplexity, BLEU, and human expert review
4. Deploy model for interactive research assistance or automated literature synthesis

**For Interdisciplinary Teams:**
1. Use SIA approach: Train specialist → Generate variations → Human review → Iterate
2. Combine quantitative metrics (from statistical analysis) with qualitative insights (from AI-generated scenarios)
3. Publish findings that integrate traditional and AI-augmented methodologies, advancing both collaboration science and computational research methods

---

## Citation & Attribution

Data generated using methodologies developed by Ben Hethslop et al. for PILAR/EUCRM research.

Symmetrical Intelligence Augmentation concept: A. Moir, 2023.

When using this data, please cite:
- The original PILAR/EUCRM theoretical framework
- The synthetic data generation approach (see `APPROACH.md`)
- Any AI models fine-tuned on this dataset

---

## Future Directions

- **Multimodal Extensions**: Pair Q&A with network diagrams of PILAR forces for visual-linguistic training
- **Cross-Cultural Validation**: Generate variants incorporating non-Western collaboration norms (e.g., Ubuntu philosophy, Confucian harmony)
- **Temporal Dynamics**: Create longitudinal datasets tracking collaboration evolution across organizational lifecycles
- **Intervention Simulation**: Develop counterfactual Q&A pairs (e.g., "What if DRA were absent?") for causal inference training

For questions or collaboration opportunities, refer to project documentation in parent directory.
