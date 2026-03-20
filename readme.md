I built a Dependency Resolver API using FastAPI. The project is structured into three layers.

First, the models layer uses Pydantic to validate incoming data. It ensures that the input follows the correct format, which is a list of dependency pairs.

Second, the logic layer contains the core algorithm. I implemented a graph using an adjacency list and used DFS with a three-state system to perform topological sorting and detect cycles. If a cycle exists, it also returns the exact cycle path.

Finally, the main API layer acts as the controller. It receives requests, validates them using the model, calls the logic function, and returns either the execution order or a cycle error. I also enabled CORS to allow frontend integration.

This separation makes the code modular, scalable, and easy to maintain.

## 🚀 Future Improvements

- 🔄 Add loading indicator for better user experience
- 🎯 Include pre-filled example inputs for quick testing
- ⚠️ Improve error messages for better clarity
- 🎨 Enhance UI with animations and modern styling
- 📊 Visualize dependency graph (nodes and edges)
- 🔍 Highlight cycle path visually in graph
- 🌐 Add support for larger real-world dependency datasets
- 🧠 Optimize performance for large inputs.
