# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# =====================================
# VjpInterface gen op list
# =====================================
# we don't support vjp function code
# gen now, so we use a whitelist to
# control the generation of Vjp methods.
# TODO(wanghao107)
# remove this file and support Vjp methods
# code gen.


vjp_interface_declare_gen_op_list = [
    'where',
    "tanh",
    "mean",
    "divide",
    "sum",
    "add",
    "concat",
    "split",
    "split_with_num",
    "gelu",
    "matmul",
    "erf",
    "multiply",
    "pow",
    "rsqrt",
    "subtract",
    "square",
    "dropout",
    'exp',
    'expm1',
    'expand',
    'layer_norm',
    'reshape',
    'cast',
    "scale",
    'softmax',
    'silu',
    'elementwise_pow',
    'embedding',
    'fused_softmax_mask_upper_triangle',
    'slice',
    'transpose',
    'slice_grad',
    'gather_nd',
    'stack',
    'poisson',
    'gumbel_softmax',
    'pad',
    'pad3d',
    'squeeze',
    'unsqueeze',
    'tril',
    'triu',
]
vjp_interface_implementation_gen_op_list = [
    'where',
    "tanh",
    "mean",
    "divide",
    "sum",
    "add",
    "concat",
    "split",
    "split_with_num",
    "gelu",
    "matmul",
    "erf",
    "multiply",
    "subtract",
    "pow",
    "rsqrt",
    "square",
    "dropout",
    'exp',
    'expm1',
    'expand',
    'layer_norm',
    'reshape',
    'cast',
    "scale",
    'softmax',
    'silu',
    'elementwise_pow',
    'embedding',
    'fused_softmax_mask_upper_triangle',
    'slice',
    'transpose',
    'slice_grad',
    'gather_nd',
    'stack',
    'poisson',
    'gumbel_softmax',
    'pad',
    'pad3d',
    'squeeze',
    'unsqueeze',
    'tril',
    'triu',
]
