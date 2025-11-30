from .resnet import resnet34, resnet50, resnet101

def build_backbone(backbone, output_stride, BatchNorm):
    if backbone == 'resnet34':
        return resnet34(output_stride=output_stride, BatchNorm=BatchNorm)
    elif backbone == 'resnet50':
        return resnet50(output_stride=output_stride, BatchNorm=BatchNorm)
    elif backbone == 'resnet101':
        return resnet101(output_stride=output_stride,BatchNorm=BatchNorm)
    else:
        raise NotImplementedError(f"Backbone '{backbone}' not implemented")