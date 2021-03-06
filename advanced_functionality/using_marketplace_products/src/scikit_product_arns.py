
class ScikitArnProvider:
    
    @staticmethod
    def get_algorithm_arn(current_region):
        mapping = {
          "ap-south-1" : "arn:aws:sagemaker:ap-south-1:077584701553:algorithm/scikit-decision-trees-15423055-57b73412d2e93e9239e4e16f83298b8f",
          "ap-northeast-2" : "arn:aws:sagemaker:ap-northeast-2:745090734665:algorithm/scikit-decision-trees-15423055-57b73412d2e93e9239e4e16f83298b8f",
          "ap-southeast-1" : "arn:aws:sagemaker:ap-southeast-1:192199979996:algorithm/scikit-decision-trees-15423055-57b73412d2e93e9239e4e16f83298b8f",
          "ap-southeast-2" : "arn:aws:sagemaker:ap-southeast-2:666831318237:algorithm/scikit-decision-trees-15423055-57b73412d2e93e9239e4e16f83298b8f",
          "ap-northeast-1" : "arn:aws:sagemaker:ap-northeast-1:977537786026:algorithm/scikit-decision-trees-15423055-57b73412d2e93e9239e4e16f83298b8f",
          "ca-central-1" : "arn:aws:sagemaker:ca-central-1:470592106596:algorithm/scikit-decision-trees-15423055-57b73412d2e93e9239e4e16f83298b8f",
          "eu-central-1" : "arn:aws:sagemaker:eu-central-1:446921602837:algorithm/scikit-decision-trees-15423055-57b73412d2e93e9239e4e16f83298b8f",
          "eu-west-1" : "arn:aws:sagemaker:eu-west-1:985815980388:algorithm/scikit-decision-trees-15423055-57b73412d2e93e9239e4e16f83298b8f",
          "eu-west-2" : "arn:aws:sagemaker:eu-west-2:856760150666:algorithm/scikit-decision-trees-15423055-57b73412d2e93e9239e4e16f83298b8f",
          "us-east-1" : "arn:aws:sagemaker:us-east-1:865070037744:algorithm/scikit-decision-trees-15423055-57b73412d2e93e9239e4e16f83298b8f",
          "us-east-2" : "arn:aws:sagemaker:us-east-2:057799348421:algorithm/scikit-decision-trees-15423055-57b73412d2e93e9239e4e16f83298b8f",
          "us-west-1" : "arn:aws:sagemaker:us-west-1:382657785993:algorithm/scikit-decision-trees-15423055-57b73412d2e93e9239e4e16f83298b8f",
          "us-west-2" : "arn:aws:sagemaker:us-west-2:594846645681:algorithm/scikit-decision-trees-15423055-57b73412d2e93e9239e4e16f83298b8f"
        }
        return mapping[current_region]
    
    
    @staticmethod
    def get_model_package_arn(current_region):
        mapping = {
          "ap-south-1": "arn:aws:sagemaker:ap-south-1:077584701553:model-package/scikit-iris-detector-154230595-8f00905c1f927a512b73ea29dd09ae30",
          "ap-northeast-2": "arn:aws:sagemaker:ap-northeast-2:745090734665:model-package/scikit-iris-detector-154230595-8f00905c1f927a512b73ea29dd09ae30",
          "ap-southeast-1" : "arn:aws:sagemaker:ap-southeast-1:192199979996:model-package/scikit-iris-detector-154230595-8f00905c1f927a512b73ea29dd09ae30",
          "ap-southeast-2" : "arn:aws:sagemaker:ap-southeast-2:666831318237:model-package/scikit-iris-detector-154230595-8f00905c1f927a512b73ea29dd09ae30",
          "ap-northeast-1" : "arn:aws:sagemaker:ap-northeast-1:977537786026:model-package/scikit-iris-detector-154230595-8f00905c1f927a512b73ea29dd09ae30",
          "ca-central-1" : "arn:aws:sagemaker:ca-central-1:470592106596:model-package/scikit-iris-detector-154230595-8f00905c1f927a512b73ea29dd09ae30",
          "eu-central-1" : "arn:aws:sagemaker:eu-central-1:446921602837:model-package/scikit-iris-detector-154230595-8f00905c1f927a512b73ea29dd09ae30",
          "eu-west-1" : "arn:aws:sagemaker:eu-west-1:985815980388:model-package/scikit-iris-detector-154230595-8f00905c1f927a512b73ea29dd09ae30",
          "eu-west-2" : "arn:aws:sagemaker:eu-west-2:856760150666:model-package/scikit-iris-detector-154230595-8f00905c1f927a512b73ea29dd09ae30",
          "us-east-1" : "arn:aws:sagemaker:us-east-1:865070037744:model-package/scikit-iris-detector-154230595-8f00905c1f927a512b73ea29dd09ae30",
          "us-east-2" : "arn:aws:sagemaker:us-east-2:057799348421:model-package/scikit-iris-detector-154230595-8f00905c1f927a512b73ea29dd09ae30",
          "us-west-1" : "arn:aws:sagemaker:us-west-1:382657785993:model-package/scikit-iris-detector-154230595-8f00905c1f927a512b73ea29dd09ae30",
          "us-west-2" : "arn:aws:sagemaker:us-west-2:594846645681:model-package/scikit-iris-detector-154230595-8f00905c1f927a512b73ea29dd09ae30"
        }
        return mapping[current_region]
