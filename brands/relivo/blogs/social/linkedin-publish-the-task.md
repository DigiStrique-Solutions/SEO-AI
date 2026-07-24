Most agent demos are synchronous. You ask, the agent grinds through every step itself, and you wait.

That breaks the moment the work is slow, external, or better handled by something else.

The fix is older than agents: a message broker.

We built it into Relivo, our open source multi namespace MCP server in Go. Five MCP servers sit behind one HTTP endpoint. One of them is an event server, a thin wrapper over a Kafka topic on Confluent Cloud.

So the agent's job changes. It stops doing the task and starts describing it.

Just publish the task. A listener downloads the skill, calls the external API, files the result. The producer owns one thing: a clear, well shaped message.

Why the broker earns its place:

→ Decoupling. The producer does not need a capability to request it. New tools appear behind the topic with zero producer changes.

→ Durability. Every task is a committed record with an offset. A listener that was down replays from where it stopped. The log is the source of truth.

→ Owner scope. Each record is stamped with the caller's API key identity, so many agents share one topic without ever reading each other's work.

→ Async fan out. Publish returns the moment the record is committed, with its partition and offset. Slow calls, retries, and rate limits live on the consumer side.

The event server is the verb. The other namespaces, memory, skills, Search Console and Product Hunt, are the vocabulary. Mount them behind one backbone and an agent can compose a task none of them offer alone: find a design skill, install it, then use it to build a page that reports today's top ranked product.

The line worth keeping: an agent that does every task is bounded by its own context and speed. An agent that publishes tasks is bounded only by how many listeners you point at the topic.

Open source, MIT licensed. Docs, quickstart and source below.

Overview: https://go-mcp-server.vercel.app/doc/overview
Event server: https://go-mcp-server.vercel.app/doc/event
Source: https://github.com/Hitesh-s0lanki/go-mcp-server

#MCP #AIAgents #Golang #Kafka #OpenSource #ModelContextProtocol
