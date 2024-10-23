def get_feedback(answer, question_number):
    # Define the acceptance criteria and prompts for each question
    prompts = {
        1: f"""
You are an expert tutor in decision-making concepts.

**Question:**
How can Tentacle Tents ensure that their evaluation of marketing channels is comprehensive and not solely focused on immediate returns, taking into account long-term benefits and brand image?

**Acceptance Criteria:**
- Discuss the importance of avoiding narrow framing.
- Explain how System 1 and System 2 thinking can be balanced.
- Mention the concept of utility beyond immediate gains.
- Suggest using a balanced scorecard approach.
- Emphasize assessing brand image impact.

**Student's Answer:**
\"\"\"
{answer}
\"\"\"

**Feedback Guidelines:**
- Begin by acknowledging what the student did well.
- Point out any missing elements from the acceptance criteria.
- Provide suggestions for improvement.
- Keep the tone positive and encouraging.

Provide constructive feedback to help the student improve their answer.
""",
        2: f"""
You are an expert tutor in decision-making concepts.

**Question:**
How might Monika Prpic's intuition affect her decision-making process in determining the most effective marketing channels? What methods can be used to validate or complement intuitive decision-making?

**Acceptance Criteria:**
- Recognize the role of System 1 thinking (intuition) and potential biases.
- Identify biases such as the halo effect and confirmation bias.
- Suggest complementing intuition with System 2 thinking (analytical methods).
- Propose decision-making tools like SWOT analysis, decision trees, A/B testing.
- Recommend involving diverse perspectives.

**Student's Answer:**
\"\"\"
{answer}
\"\"\"

**Feedback Guidelines:**
- Acknowledge strengths in the student's response.
- Highlight any missing or underdeveloped points from the acceptance criteria.
- Offer specific advice on how to enhance the answer.
- Maintain a supportive tone.

Provide constructive feedback to help the student improve their answer.
""",
        3: f"""
You are an expert tutor in decision-making concepts.

**Question:**
What strategies could Tentacle Tents employ to avoid becoming overly committed to past decisions or investments that may not be yielding the desired results?

**Acceptance Criteria:**
- Recognize the sunk cost fallacy.
- Address loss aversion.
- Suggest implementing regular performance reviews.
- Promote a culture of flexibility.
- Set clear exit criteria.
- Propose separating decision-making roles.

**Student's Answer:**
\"\"\"
{answer}
\"\"\"

**Feedback Guidelines:**
- Praise the aspects the student covered well.
- Identify any key strategies they missed.
- Provide guidance on how to cover missing points.
- Encourage them to think critically.

Provide constructive feedback to help the student improve their answer.
""",
        4: f"""
You are an expert tutor in decision-making concepts.

**Question:**
What factors should Tentacle Tents consider in their evaluation of what would be effective for their own brand, and how can they maintain an independent perspective?

**Acceptance Criteria:**
- Avoid the bandwagon effect.
- Understand the unique value proposition.
- Conduct internal analysis (e.g., SWOT analysis).
- Engage in market research.
- Utilize independent thinking.
- Consult external experts.

**Student's Answer:**
\"\"\"
{answer}
\"\"\"

**Feedback Guidelines:**
- Recognize the student's good points.
- Mention any factors they overlooked.
- Suggest how to deepen their analysis.
- Keep feedback constructive.

Provide constructive feedback to help the student improve their answer.
""",
        5: f"""
You are an expert tutor in decision-making concepts.

**Question:**
How can Tentacle Tents ensure that their decision-making process takes into account the perspectives and preferences of different customer segments, without overemphasizing one particular group?

**Acceptance Criteria:**
- Avoid narrow framing.
- Use segmented data analysis.
- Develop weighted decision criteria.
- Create customer personas.
- Implement inclusive decision-making processes.
- Monitor market trends across segments.
- Use multi-criteria decision analysis (MCDA).

**Student's Answer:**
\"\"\"
{answer}
\"\"\"

**Feedback Guidelines:**
- Highlight strengths in the student's response.
- Point out missing elements.
- Provide suggestions for covering all customer segments.
- Encourage inclusivity in decision-making.

Provide constructive feedback to help the student improve their answer.
"""
    }

    prompt = prompts.get(question_number, "Provide feedback on the student's answer.")

    try:
        response = client.chat.completions.create(
            model=MODEL,
            prompt=prompt,
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0,
        )
        feedback = response.choices[0].text.strip()
    except Exception as e:
        feedback = "An error occurred while generating feedback. Please try again."

    return feedback
