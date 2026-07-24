Most agent demos do the task. The better move is to publish it.

We built an event server into Relivo, our open source multi namespace MCP server in Go. It is a thin wrapper over a Kafka topic. The agent stops doing the work and just describes it, then a listener downloads the skill or calls the API and files the result.

What that buys you:

→ Decoupling. New tools appear behind the topic with zero producer changes.
→ Durability. Every task is a committed record with an offset. A listener that was down replays from where it stopped.
→ Owner scope. Each record is stamped with the caller's API key, so many agents share one topic without reading each other's work.

An agent that does every task is bounded by its own speed. An agent that publishes tasks is bounded only by how many listeners you point at the topic.

Open source, MIT licensed.
Docs: https://go-mcp-server.vercel.app/doc/event
Source: https://github.com/Hitesh-s0lanki/go-mcp-server

#MCP #AIAgents #Golang #Kafka #OpenSource
