# coding=utf-8
# Copyright 2021 The Google Research Authors.
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

"""This package provides core layers for ETC.

Users of ETC can import this package directly and refer to invidual layer
classes exposed from this file, for example:

  from etcmodel import layers as etc_layers

  my_layer = etc_layers.GlobalLocalTransformerLayers(...)
"""

from etclayers import attention
from etclayers import embedding
from etclayers import helpers
from etclayers import recomputing_dropout
from etclayers import transformer
from etclayers import wrappers

GlobalLocalTransformerLayers = transformer.GlobalLocalTransformerLayers
RelativeTransformerLayers = transformer.RelativeTransformerLayers

EmbeddingLookup = embedding.EmbeddingLookup

DenseLayers = helpers.DenseLayers
TrackedLambda = helpers.TrackedLambda

ResidualBlock = wrappers.ResidualBlock

RecomputingDropout = recomputing_dropout.RecomputingDropout

RelativeAttention = attention.RelativeAttention
FusedGlobalLocalAttention = attention.FusedGlobalLocalAttention
ProjectAttentionHeads = attention.ProjectAttentionHeads
QkvRelativeAttention = attention.QkvRelativeAttention
QkvRelativeLocalAttention = attention.QkvRelativeLocalAttention
