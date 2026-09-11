# Copyright (c) 2026 The Qwen team, Alibaba Group.
# Licensed under The MIT License [see LICENSE for details]

try:
    from .gated_delta_rule import chunk_gated_delta_rule
except ValueError as exc:
    if "sm90" not in str(exc).lower():
        raise
    chunk_gated_delta_rule = None


__all__ = ["chunk_gated_delta_rule"]
