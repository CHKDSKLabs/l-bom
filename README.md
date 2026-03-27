---
title: L-BOM
emoji: 💘`
colorFrom: pink
colorTo: red
sdk: static
pinned: true
---

## L-BOM - Local LLM Software Bill of Materials CLI

`L-BOM` is a small Python CLI that inspects local LLM model artifacts such as `.gguf` and `.safetensors` files and emits a lightweight Software Bill of Materials (SBOM) with file identity, format details, model metadata, and parsing warnings. `L-BOM` has a sister program, [`GUI-BOM`](https://github.com/CHKDSKLabs/gui-bom) that wraps it in a friendly GUI and makes it easy to deploy.

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

Scan a single model file and emit a huggingface-style README:

```bash
l-bom scan .\models\Llama-3.1-8B-Instruct-Q4_K_M.gguf --format hf-readme
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

## Sample JSON output

Sample JSON output for (`LFM2.5-1.2B-Instruct-Q8_0.gguf`)[https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct-GGUF]:

```json
{
  "sbom_version": "1.0",
  "generated_at": "2026-03-25T04:07:53.262551+00:00",
  "tool_name": "l-bom",
  "tool_version": "0.1.0",
  "model_path": "C:\\models\\LFM2.5-1.2B-Instruct-GGUF\\LFM2.5-1.2B-Instruct-Q8_0.gguf",
  "model_filename": "LFM2.5-1.2B-Instruct-Q8_0.gguf",
  "file_size_bytes": 1246253888,
  "sha256": "f6b981dcb86917fa463f78a362320bd5e2dc45445df147287eedb85e5a30d26a",
  "format": "gguf",
  "architecture": "lfm2",
  "parameter_count": 1170340608,
  "quantization": "Q5_1",
  "dtype": null,
  "context_length": 128000,
  "vocab_size": 65536,
  "license": null,
  "base_model": null,
  "training_framework": null,
  "metadata": {
    "general.architecture": "lfm2",
    "general.type": "model",
    "general.name": "4cd563d5a96af9e7c738b76cd89a0a200db7608f",
    "general.finetune": "4cd563d5a96af9e7c738b76cd89a0a200db7608f",
    "general.size_label": "1.2B",
    "general.license": "other",
    "general.license.name": "lfm1.0",
    "general.license.link": "LICENSE",
    "general.tags": [
      "liquid",
      "lfm2.5",
      "edge",
      "text-generation"
    ],
    "general.languages": [
      "en",
      "ar",
      "zh",
      "fr",
      "de",
      "ja",
      "ko",
      "es"
    ],
    "lfm2.block_count": 16,
    "lfm2.context_length": 128000,
    "lfm2.embedding_length": 2048,
    "lfm2.feed_forward_length": 8192,
    "lfm2.attention.head_count": 32,
    "lfm2.attention.head_count_kv": [
      0,
      0,
      8,
      0,
      0,
      8,
      0,
      0,
      8,
      0,
      8,
      0,
      8,
      0,
      8,
      0
    ],
    "lfm2.rope.freq_base": 1000000.0,
    "lfm2.attention.layer_norm_rms_epsilon": 9.999999747378752e-06,
    "lfm2.vocab_size": 65536,
    "lfm2.shortconv.l_cache": 3,
    "tokenizer.ggml.model": "gpt2",
    "tokenizer.ggml.pre": "lfm2",
    "tokenizer.ggml.tokens": {
      "type": "array",
      "element_type": "STRING",
      "count": 65536,
      "preview": [
        "<|pad|>",
        "<|startoftext|>",
        "<|endoftext|>",
        "<|fim_pre|>",
        "<|fim_mid|>",
        "<|fim_suf|>",
        "<|im_start|>",
        "<|im_end|>",
        "<|tool_list_start|>",
        "<|tool_list_end|>",
        "<|tool_call_start|>",
        "<|tool_call_end|>",
        "<|tool_response_start|>",
        "<|tool_response_end|>",
        "<|reserved_4|>",
        "<|reserved_5|>"
      ],
      "truncated": true
    },
    "tokenizer.ggml.token_type": {
      "type": "array",
      "element_type": "INT32",
      "count": 65536,
      "preview": [
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        1,
        1
      ],
      "truncated": true
    },
    "tokenizer.ggml.merges": {
      "type": "array",
      "element_type": "STRING",
      "count": 63683,
      "preview": [
        "Ċ Ċ",
        "Ċ ĊĊ",
        "ĊĊ Ċ",
        "Ċ ĊĊĊ",
        "ĊĊ ĊĊ",
        "ĊĊĊ Ċ",
        "Ċ ĊĊĊĊ",
        "ĊĊ ĊĊĊ",
        "ĊĊĊ ĊĊ",
        "ĊĊĊĊ Ċ",
        "Ċ ĊĊĊĊĊ",
        "ĊĊ ĊĊĊĊ",
        "ĊĊĊ ĊĊĊ",
        "ĊĊĊĊ ĊĊ",
        "ĊĊĊĊĊ Ċ",
        "Ċ ĊĊĊĊĊĊ"
      ],
      "truncated": true
    },
    "tokenizer.ggml.bos_token_id": 1,
    "tokenizer.ggml.eos_token_id": 7,
    "tokenizer.ggml.padding_token_id": 0,
    "tokenizer.ggml.add_bos_token": true,
    "tokenizer.ggml.add_sep_token": false,
    "tokenizer.ggml.add_eos_token": false,
    "tokenizer.chat_template": "{{- bos_token -}}\n{%- set keep_past_thinking = keep_past_thinking | default(false) -%}\n{%- set ns = namespace(system_prompt=\"\") -%}\n{%- if messages[0][\"role\"] == \"system\" -%}\n    {%- set ns.system_prompt = messages[0][\"content\"] -%}\n    {%- set messages = messages[1:] -%}\n{%- endif -%}\n{%- if tools -%}\n    {%- set ns.system_prompt = ns.system_prompt + (\"\\n\" if ns.system_prompt else \"\") + \"List of tools: [\" -%}\n    {%- for tool in tools -%}\n        {%- if tool is not string -%}\n            {%- set tool = tool | tojson -%}\n        {%- endif -%}\n        {%- set ns.system_prompt = ns.system_prompt + tool -%}\n        {%- if not loop.last -%}\n            {%- set ns.system_prompt = ns.system_prompt + \", \" -%}\n        {%- endif -%}\n    {%- endfor -%}\n    {%- set ns.system_prompt = ns.system_prompt + \"]\" -%}\n{%- endif -%}\n{%- if ns.system_prompt -%}\n    {{- \"<|im_start|>system\\n\" + ns.system_prompt + \"<|im_end|>\\n\" -}}\n{%- endif -%}\n{%- set ns.last_assistant_index = -1 -%}\n{%- for message in messages -%}\n    {%- if message[\"role\"] == \"assistant\" -%}\n        {%- set ns.last_assistant_index = loop.index0 -%}\n    {%- endif -%}\n{%- endfor -%}\n{%- for message in messages -%}\n    {{- \"<|im_start|>\" + message[\"role\"] + \"\\n\" -}}\n    {%- set content = message[\"content\"] -%}\n    {%- if content is not string -%}\n        {%- set content = content | tojson -%}\n    {%- endif -%}\n    {%- if message[\"role\"] == \"assistant\" and not keep_past_thinking and loop.index0 != ns.last_assistant_index -%}\n        {%- if \"</think>\" in content -%}\n            {%- set content = content.split(\"</think>\")[-1] | trim -%}\n        {%- endif -%}\n    {%- endif -%}\n    {{- content + \"<|im_end|>\\n\" -}}\n{%- endfor -%}\n{%- if add_generation_prompt -%}\n    {{- \"<|im_start|>assistant\\n\" -}}\n{%- endif -%}",
    "general.quantization_version": 2,
    "general.file_type": 7,
    "gguf_version": 3,
    "endianness": "little",
    "metadata_keys": [
      "general.architecture",
      "general.type",
      "general.name",
      "general.finetune",
      "general.size_label",
      "general.license",
      "general.license.name",
      "general.license.link",
      "general.tags",
      "general.languages",
      "lfm2.block_count",
      "lfm2.context_length",
      "lfm2.embedding_length",
      "lfm2.feed_forward_length",
      "lfm2.attention.head_count",
      "lfm2.attention.head_count_kv",
      "lfm2.rope.freq_base",
      "lfm2.attention.layer_norm_rms_epsilon",
      "lfm2.vocab_size",
      "lfm2.shortconv.l_cache",
      "tokenizer.ggml.model",
      "tokenizer.ggml.pre",
      "tokenizer.ggml.tokens",
      "tokenizer.ggml.token_type",
      "tokenizer.ggml.merges",
      "tokenizer.ggml.bos_token_id",
      "tokenizer.ggml.eos_token_id",
      "tokenizer.ggml.padding_token_id",
      "tokenizer.ggml.add_bos_token",
      "tokenizer.ggml.add_sep_token",
      "tokenizer.ggml.add_eos_token",
      "tokenizer.chat_template",
      "general.quantization_version",
      "general.file_type"
    ],
    "tensor_count": 148,
    "tensor_type_counts": {
      "Q8_0": 93,
      "F32": 55
    },
    "tensor_type_parameter_counts": {
      "Q8_0": 1170210816,
      "F32": 129792
    }
  },
  "warnings": []
}
```

## Sample Huggingface Output

Sample hf-readme output for (`LFM2.5-1.2B-Instruct-Q8_0.gguf`)[https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct-GGUF]:

```markdown
---
title: "LFM2.5-1.2B-Instruct-Q8_0"
short_description: "GGUF model artifact for LFM2.5-1.2B-Instruct-Q8_0 with 1.17B parameters, 1.2B, Q5_1, 128.00K context"
tags:
  - "liquid"
  - "lfm2.5"
  - "edge"
  - "text-generation"
  - "gguf"
  - "lfm2"
  - "q5_1"
---

# LFM2.5-1.2B-Instruct-Q8_0

GGUF model artifact for LFM2.5-1.2B-Instruct-Q8_0 with 1.17B parameters, 1.2B, Q5_1, 128.00K context

This README content was generated by `L-BOM` from a local model artifact.

## Artifact details

- **Filename:** `LFM2.5-1.2B-Instruct-Q8_0.gguf`
- **Path:** `C:\models\LFM2.5-1.2B-Instruct-GGUF\LFM2.5-1.2B-Instruct-Q8_0.gguf`
- **Format:** `gguf`
- **File size:** `1.16 GiB` (1,246,253,888 bytes)
- **SHA256:** `f6b981dcb86917fa463f78a362320bd5e2dc45445df147287eedb85e5a30d26a`
- **Architecture:** `lfm2`
- **Parameters:** `1,170,340,608` (1.17B)
- **Size label:** `1.2B`
- **Quantization:** `Q5_1`
- **Context length:** `128,000`
- **Vocabulary size:** `65,536`

## Model metadata

- **License:** `lfm1.0`
- **License reference:** `LICENSE`
- **Languages:** `en`, `ar`, `zh`, `fr`, `de`, `ja`, `ko`, `es`
- **Tags:** `liquid`, `lfm2.5`, `edge`, `text-generation`, `gguf`, `lfm2`, `q5_1`
Generated with L-BOM. Contribute to L-BOM 💘 development: https://github.com/CHKDSKLabs/l-bom
```

## License

This project is licensed under the MIT License. See `LICENSE` for the full text.
