"""

# What are LLM Evals?

LLM evals are systematic, repeatable tests used to judge an LLM or LLM-powered system against a clear criteria.

## Systematic

It should not be random prompting.

Instead of asking 5 questions casually and saying looks good, we create planned test cases.

For example:

* 100 real student doubts for a CampusX course assistant.

## Repeatable

The same eval should be runnable again.

If we change the prompt, model, retriever, chunking strategy, or system instruction, we should be able to run the same test again and compare results.

This is how we know whether the system improved or became worse.

# Clear criteria

We must define what good means.

For example, for a CampusX course assistant, a good answer should be:

* correct
* simple explanation
* grounded in course content
* safe and policy-compliant

Without criteria, we are only judging by vibes.

---

An eval is not just a metric. An eval is the complete testing setup. It includes:

* What are we evaluating?
* What does good mean?
* What test cases are we using?
* How are we judging the output?
* When are we running it?
* Which tool are we using?

We are talking about the complete process of testing an LLM-powered system in a structured way.

The goal is not just to get a score. The goal is to answer practical questions like:

- Can the model be used for a particular task/application?
- Is this system good enough to ship?
- Did prompt v2 improve over prompt v1?
- Is the RAG answer grounded in the retrieved context?
- Is the agent completing the task correctly?
- Is the chatbot safe for real users?
- Is the latency under control?

LLM Evals
    - Model Evals
    - Application Evals

- Model Evals

Model evals evaluate the model itself. The main idea is to test and evaluate the capabilities of a model.

Some important capabilities include:

- Reasoning: Can it reason?
- Knowledge: Can it answer knowledge-based questions?
- Maths: Can it solve maths problems
- Coding: Can it write code
- Instruction Following: Can it follow instructions
- Long Context: Can it follow long documents
- Multimodal understanding: Can it understand images
- Tool-use: Can it use tools

- Application Evals

Application evals assess the behaviour and performance of an LLM-powered application, whether at the level of the entire system or a specific component within it.

In application eval we don't ask:
Can the model do this?

Instead application eval tells whether the product works.

For example, suppose we build a CampusX course assistant.

Application evals ask:

- Did it answer the student's question correctly?
- Did it use the course material properly?
- Was the answer faithful to the retrieved context?
- Was it clear for a beginner?
- Did it avoid hallucinating policies?
- Did it respond quickly enough?
- Did it stay safe?

"""

