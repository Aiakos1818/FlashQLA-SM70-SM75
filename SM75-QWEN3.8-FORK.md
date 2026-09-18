# SM75 / Qwen3.8-27B FlashQLA fork

This fork carries the FlashQLA changes used by
[Aiakos1818/qwen3-8-27b-dual-2080ti-vllm](https://github.com/Aiakos1818/qwen3-8-27b-dual-2080ti-vllm)
to run the Qwen3.8-27B GDN / linear-attention prefill on 2 × RTX 2080 Ti 22GB
(Turing / SM75, NVLink, TP=2).

- **Base**: upstream `main` = `3ab27d77d8ca01d7a4718903b726add1a8886c0e`.
- **Branch**: `2080ti_dual_qwen38-27B` (same name as the deployment repo's branch).
- **Change**:
  - tolerate a missing SM90 chunk kernel at import time (degrade to `None` and
    use the `flashqla_legacy` GDN backend on Turing);
  - build the legacy GDN extension for SM75 only (`TORCH_CUDA_ARCH_LIST=7.5`).

Used together with the vLLM fork
[Aiakos1818/vllm@2080ti_dual_qwen38-27B](https://github.com/Aiakos1818/vllm/tree/2080ti_dual_qwen38-27B).
See the deployment repo above for patches, design docs and launch scripts.

## License

MIT (upstream FlashQLA-SM70-SM75).
