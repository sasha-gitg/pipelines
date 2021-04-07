# Copyright 2021 Google LLC. All Rights Reserved.
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
"""Core modules for AI Platform Components."""

from google.cloud import aiplatform
from google_cloud_components.aiplatform import utils

DatasetCreateOp = utils.convert_method_to_component(
	aiplatform.Dataset.create)

DatasetExportDataOp = utils.convert_method_to_component(
	aiplatform.Dataset.export_data,
	should_serialize_init=True)

ImageDatasetCreateOp = utils.convert_method_to_component(
	aiplatform.ImageDataset.create)

TabularDatasetCreateOp = utils.convert_method_to_component(
	aiplatform.TabularDataset.create)

TextDatasetCreateOp = utils.convert_method_to_component(
	aiplatform.TextDataset.create)

VideoDatasetCreateOp = utils.convert_method_to_component(
	aiplatform.VideoDataset.create)

ImageDatasetImportDataOp = utils.convert_method_to_component(
	aiplatform.ImageDataset.import_data, should_serialize_init=True)

TabularDatasetImportDataOp = utils.convert_method_to_component(
	aiplatform.TabularDataset.import_data, should_serialize_init=True)

TextDatasetImportDataOp = utils.convert_method_to_component(
	aiplatform.TextDataset.import_data, should_serialize_init=True)

VideoDatasetImportDataOp = utils.convert_method_to_component(
	aiplatform.VideoDataset.import_data, should_serialize_init=True)

CustomContainerTrainingJobRunOp = utils.convert_method_to_component(
	aiplatform.CustomContainerTrainingJob.run,
    should_serialize_init=True)

CustomPythonPackageTrainingJobRunOp = utils.convert_method_to_component(
	aiplatform.CustomPythonPackageTrainingJob.run,
    should_serialize_init=True)

AutoMLImageTrainingJobRunOp = utils.convert_method_to_component(
	aiplatform.AutoMLImageTrainingJob.run,
	should_serialize_init=True)

AutoMLTextTrainingJobRunOp = utils.convert_method_to_component(
	aiplatform.AutoMLTextTrainingJob.run,
	should_serialize_init=True)

AutoMLTabularTrainingJobRunOp = utils.convert_method_to_component(
	aiplatform.AutoMLTabularTrainingJob.run,
	should_serialize_init=True)

AutoMLVideoTrainingJobRunOp = utils.convert_method_to_component(
	aiplatform.AutoMLVideoTrainingJob.run,
	should_serialize_init=True)

ModelDeployOp = utils.convert_method_to_component(
	aiplatform.Model.deploy,
	should_serialize_init=True)

ModelBatchPredictOp = utils.convert_method_to_component(
	aiplatform.Model.batch_predict,
	should_serialize_init=True)

ModelUploadOp = utils.convert_method_to_component(
	aiplatform.Model.upload)

EndpointCreateOp = utils.convert_method_to_component(
	aiplatform.Endpoint.create)
