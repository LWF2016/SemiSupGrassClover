from .resnet import ResNet34, ResNet50, ResNet101

def build_backbone(backbone, output_stride, BatchNorm):
    if backbone == 'resnet34' or backbone == 'resnet':
        return ResNet34(output_stride=output_stride, BatchNorm=BatchNorm)
    elif backbone == 'resnet50':
        return ResNet50(output_stride=output_stride, BatchNorm=BatchNorm)
    elif backbone == 'resnet101':
        return ResNet101(output_stride=output_stride,BatchNorm=BatchNorm)
    else:
        raise NotImplementedError(f"Backbone '{backbone}' not implemented")