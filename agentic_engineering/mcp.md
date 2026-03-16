# Model Context Protocol

- A way of giving AI agents access to external tools to be able to make them execute tasks (run a db query) rather than just question/answer(chat).

- MCP exposes a set of tools(RPC function) to the LLM with its documentation. When called with expected parameters it returns a response.

- Modern LLMs are fine tuned to use tools by outputting text in a certain format to be able to invoke the tool. The agentic orchestration software invoking the LLM can use these tool call output and invokes the tools(here using mcp client for example). Tool call results are fed back to the LLM as part of its context.

- LLM generates stream of tokens. Token could be a word, a syllable, punctuation or some text. Given the output is a stream of tokens, LLM outputs with a special token that indicates the starting of a tool call and another special token indicating the end of the tool call(think HTML tags). Within these start and end tokens, the content is a JSON message describing the tool call (which tool, what parameters to pass)

```text
<|tool_call|>
{
  "name": "get_current_weather",
  "arguments": {
    "location": "Austin, TX, USA"
  }
}
<|end_tool_call|>
```

`Agent → Harness → LLM API`

- LLM's Harness, when it sees the stream of tokens indicating a tool call, it pauses the LLM from generating and this information is passed to the agent via structured API result. Agent invokes the MCP tool, sends the result back to the Harness. LLM Harness will use another set of special tokens to feed to the LLM to know that this was the result of the tool call.

```text
<|tool_result|>
{
  "location": "Austin, TX, USA",
  "temperature": 93,
  "unit": "fahrenheit",
  "conditions": "sunny"
}
<|end_tool_result|>
```

---

## References

- [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro)
