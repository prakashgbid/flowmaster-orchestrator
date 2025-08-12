# Installation

## Requirements

- Python 3.8 or higher
- pip package manager

## Installation Methods

### From GitHub

```bash
pip install git+https://github.com/prakashgbid/osa-langgraph-orchestrator.git
```

### From Source

```bash
git clone https://github.com/prakashgbid/osa-langgraph-orchestrator.git
cd osa-langgraph-orchestrator
pip install -e .
```

### Development Installation

```bash
git clone https://github.com/prakashgbid/osa-langgraph-orchestrator.git
cd osa-langgraph-orchestrator
pip install -e ".[dev]"
```

## Verify Installation

```python
import langgraph_orchestrator
print(langgraph_orchestrator.__version__)
```
