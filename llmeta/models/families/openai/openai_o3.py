# filename: openai_o3.py
# @Time    : 2025/11/8 13:33
# @Author  : JQQ
# @Email   : jiaqia@qknode.com
# @Software: PyCharm
from llmeta.capabilities import ModelCapabilities
from llmeta.models.base import ModelFamily
from llmeta.models.config import ModelFamilyConfig, SpecificModelConfig
from llmeta.provider import Provider

# ============================================================================
# O3 系列 / O3 Series
# ============================================================================


O3 = ModelFamilyConfig(
    family=ModelFamily.O3,
    provider=Provider.OPENAI,
    version_default="3.0",
    patterns=[
        "o3-{variant}-{year:4d}-{month:2d}-{day:2d}",
        "o3-{variant}",
        "o3-{year:4d}-{month:2d}-{day:2d}",
        "o3",
    ],
    capabilities=ModelCapabilities(
        supports_streaming=True,
        supports_function_calling=True,
        supports_structured_outputs=True,
    ),
    specific_models={
        "o3": SpecificModelConfig(
            version="3.0",
            variant="base",
            capabilities=ModelCapabilities(
                supports_streaming=True,
                supports_function_calling=True,
                supports_structured_outputs=True,
            ),
            patterns=[
                "o3-{year:4d}-{month:2d}-{day:2d}",
                "o3",
            ],
        ),
        "o3-mini": SpecificModelConfig(
            version="3.0",
            variant="mini",
            capabilities=ModelCapabilities(
                supports_streaming=True,
                supports_function_calling=True,
                supports_structured_outputs=True,
            ),
            patterns=[
                "o3-mini-{year:4d}-{month:2d}-{day:2d}",
                "o3-mini",
            ],
        ),
        "o3-pro": SpecificModelConfig(
            version="3.0",
            variant="pro",
            capabilities=ModelCapabilities(
                supports_streaming=False,
                supports_function_calling=True,
                supports_structured_outputs=True,
            ),
            patterns=[
                "o3-pro-{year:4d}-{month:2d}-{day:2d}",
                "o3-pro",
            ],
        ),
        "o3-deep-research": SpecificModelConfig(
            version="3.0",
            variant="deep-research",
            capabilities=ModelCapabilities(
                supports_streaming=True,
                supports_function_calling=False,
                supports_structured_outputs=False,
            ),
            patterns=[
                "o3-deep-research-{year:4d}-{month:2d}-{day:2d}",
                "o3-deep-research",
            ],
        ),
    },
)
