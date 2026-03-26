---
title: L Bom 
emoji: 💘
colorFrom: pink
colorTo: red
sdk: static
pinned: true
---

## L-BOM 💘: Local LLM Software Bill of Materials

`L-BOM` is a small Python CLI that inspects local LLM model artifacts such as `.gguf` and `.safetensors` files and emits a lightweight Software Bill of Materials (SBOM) with file identity, format details, model metadata, and parsing warnings.

### Install

```bash
pip install .
```

For editable local development:

```bash
pip install -e .
```

### Usage

Show the installed version:

```bash
l-bom version
```

Scan a single model file and emit JSON:

```bash
l-bom scan .\models\Llama-3.1-8B-Instruct-Q4_K_M.gguf
```

Scan a single model file and emit SPDX tag-value:

```bash
l-bom scan .\models\Llama-3.1-8B-Instruct-Q4_K_M.gguf --format spdx
```

Scan a directory recursively and render a Rich table:

```bash
l-bom scan .\models --format table
```

Export a single model scan as Hugging Face-ready `README.md` content:

```bash
l-bom scan .\models\Llama-3.1-8B-Instruct-Q4_K_M.gguf --format hf-readme --hf-sdk static --hf-app-file index.html
```

Override the inferred title and short description for the README front matter:

```bash
l-bom scan .\models\Llama-3.1-8B-Instruct-Q4_K_M.gguf --format hf-readme --hf-title "Llama 3.1 Demo" --hf-short-description "Quantized GGUF artifact for a local demo space"
```

Skip SHA256 hashing for very large files and write the result to disk:

```bash
l-bom scan .\models --no-hash --output .\model-sbom.json
```

### Sample JSON output

```json
{
  "sbom_version": "1.0",
  "generated_at": "2026-03-24T14:08:22.118000+00:00",
  "tool_name": "L-BOM",
  "tool_version": "0.1.0",
  "model_path": "C:\\models\\Llama-3.1-8B-Instruct-Q4_K_M.gguf",
  "model_filename": "Llama-3.1-8B-Instruct-Q4_K_M.gguf",
  "file_size_bytes": 4682873912,
  "sha256": "8b0b3cb15be2e0a0f4b474230ef326f6180fc76efad1d761bf9ce949f6e785b4",
  "format": "gguf",
  "architecture": "llama",
  "parameter_count": 8030261248,
  "quantization": "Q4_K_M",
  "dtype": null,
  "context_length": 8192,
  "vocab_size": 128256,
  "license": "llama3.1",
  "base_model": "meta-llama/Llama-3.1-8B-Instruct",
  "training_framework": "transformers 4.43.2",
  "metadata": {
    "general.name": "Llama 3.1 8B Instruct",
    "general.file_type": 14,
    "gguf_version": 3,
    "endianness": "little",
    "metadata_keys": [
      "general.architecture",
      "general.file_type",
      "llama.context_length",
      "tokenizer.ggml.tokens"
    ],
    "sidecar_config": {
      "model_type": "llama",
      "architectures": [
        "LlamaForCausalLM"
      ],
      "torch_dtype": "bfloat16",
      "transformers_version": "4.43.2"
    }
  },
  "warnings": []
}
```

### License

This project is licensed under the MIT License. See `LICENSE` for the full text.
