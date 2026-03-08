# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").


```markdown
**Answer:** 
The game was impossible to win, the hints did not help the game development, they seemed to be swapped. The button `new game` was not working.

```


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

```markdown
**Answer:** 
I used Claude Sonnet from VS code Copilot. It suggested checking the `check_guess` function and the `get_range_for_difficulty`
Ii suggested checking the `New Game` button. But it does not explain why it does not reset the game.

```

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
```markdown
**Answer:**
Most of the bus were fixed by testing the game manually. The logic behind the functions in `logic_utils.py` were tested using pytest. The tests showed that the logic was correct, but the game was not working as expected. AI helped me understand the tests and design better ones.
```

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?
```markdown
**Answer:**
The secret number kept changing because it was being generated on every rerun of the game, somehow this was intended. I would explain it by saying that Streamlit rerun the script each time there is an interacion. Therefore, flags are required to decide what to print and when. In my opinion, giving a secret that is fixed with the `New Game` button is not the best solution. I thought it'd be better to update it each time the game is initialized.
```

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
- This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
`````markdown*
*Answer:**
I want to reuse the habit of testing the code manually and using pytest to test, it helps in bigscale projects where features are added but you want to keep certain behavior. I'd say I would do better asking some questions to the AI, I think I was not specific enough in some of my prompts and also it is required to understand what's going under the hood. 
I think it changed the way by making me ask better questions and keep track of the suggestions but being critical about them, not all suggestions are good and it is required to understand the code to know if the suggestion is good or not.
```