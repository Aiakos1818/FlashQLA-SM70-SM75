# Copyright (c) 2026 The Qwen team, Alibaba Group.
# Licensed under The MIT License [see LICENSE for details]

__version__ = "0.1.0"

try:
    from flash_qla.ops.gated_delta_rule.chunk import (
        chunk_gated_delta_rule_fwd,
        chunk_gated_delta_rule_bwd,
        chunk_gated_delta_rule,
    )
except ValueError as exc:
    if "sm90" not in str(exc).lower():
        raise
    chunk_gated_delta_rule_fwd = None
    chunk_gated_delta_rule_bwd = None
    chunk_gated_delta_rule = None

__all__ = [
    "chunk_gated_delta_rule_fwd",
    "chunk_gated_delta_rule_bwd",
    "chunk_gated_delta_rule",
]
