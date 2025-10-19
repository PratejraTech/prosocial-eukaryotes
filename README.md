# Psych-Prosocial Research

This project explores prosocial behavior and collaboration dynamics through evolutionary psychology, sociobiology, and social/group psychology. It develops the PILAR model (Prospects, Involved, Liked, Agency, Respect) to encapsulate over 30 SGP theories for assessing collaboration viability in complex environments.

## Directory Structure

- `apriori-research-summaries/`: Contains hypotheses and research summaries.
- `docs/`: Documentation and summations.
- `processing/`: Python scripts for processing research documents, including PDF to Markdown conversion.
- `research-compilar/`: Compiled research papers and abstracts.
- `vector/`: Vector database implementation for document search.

## Hypotheses

H1: Teaching PILAR/EUCRM increases prosocial orientation and group viability, mediated by pillar awareness; stronger in low-empathy individuals.

H2: High inequality aversion predicts elevated Respect/Involved perceptions and prosocial engagement, moderating zero-sum avoidance.

H3: Egalitarian structures boost liking/respect/communication but reduce agency/confidence, leading to stable yet less adaptive groups in resource-scarce ecologies.

H4: Low prosociality causes reticence in prosocial learning, requiring ancestral norm priming for engagement.

H5: Hierarchy steepness balances confidence/performance vs. trio feedback; optimal in actualization hierarchies.

## Paths Forward

1. Evaluate abstracts and research papers to develop rigorous hypotheses tested by deep research agents.
2. Use BMAD method to produce requirements for collaborative software or operation instructions optimizing collaboration in complex environments.
3. Develop three case studies based on research in complex environments.
4. Draw in pre-eminent researchers on prosocial development from the 19th and 20th centuries.
5. Stick to BMAD method, assuming incorrect until logically sound conclusions.

## Technical Implementation

Research documents are processed by chunking text and upserting vectors into ChromaDB using LlamaIndex for efficient retrieval and analysis.