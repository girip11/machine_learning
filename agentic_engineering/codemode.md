# Code mode

- Agents use the MCP by exposing the tools available to the LLM.

- Cloudfare converted MCP tools to typescript api and made the llm write code that calls these api. This is referred to as code mode. This worked much better compared to calling tools available from the MCP servers.

- Converting MCP tools to api resulted in enabling the LLM to handle many tools and complex tools.
- Multiple tool calls can now be chained inside the code. Faster and less token consumption as the intermediate results of the tool calls now become return values of those apis handled in the code. Only final results are given back to the LLM.

> In short, LLMs are better at writing code to call MCP, than at calling MCP directly.
>Meanwhile, LLMs are getting really good at writing code. In fact, LLMs asked to write code against the full, complex APIs normally exposed to developers don't seem to have too much trouble with it. Why, then, do MCP interfaces have to "dumb it down"? Writing code and calling tools are almost the same thing, but it seems like LLMs can do one much better than the other?
>The answer is simple: LLMs have seen a lot of code. They have not seen a lot of "tool calls". In fact, the tool calls they have seen are probably limited to a contrived training set constructed by the LLM's own developers, in order to try to train it. Whereas they have seen real-world code from millions of open source projects.

- MCP server tools are converted to say python or typescript APIs(CLI tools with say --help) and then with progressive disclosure, LLMs can use the api help to find the parameters and then write code which could be a chain of tool calls(cli calls) that can be run in a sandboxed environment.

- We have got tools like [`Monty`](https://github.com/pydantic/monty) which is a python subset interpreter mainly created to act as a sandbox environment for executing the python code written by the LLMs.

- Minimal agent library like [smolagents](https://github.com/huggingface/smolagent) support CodeAgent which operates primarily in the code mode, apart from supporting traditional tool call.

---

## References

- [Code Mode: The better way to use MCP](https://blog.cloudflare.com/code-mode/)
