import math

height = int(input('what is the input height?'))
width = int(input('what is the input width?'))
padding_height = int(input('what is the padding height?'))
padding_width = int(input('what is the padding width?'))
dilation_height = int(input('what is the dilation height?'))
dilation_width = int(input('what is the dilation width?'))
kernel_height = int(input('what is the kernel height?'))
kernel_width = int(input('what is the kernel width?'))
stride_height = int(input('what is the stride height?'))
stride_width = int(input('what is the stride width?'))

height_out = (height - 1) * stride_height - 2 * padding_height + dilation_height * (kernel_height - 1) + padding_height + 1
width_out = (width - 1) * stride_width - 2 * padding_width + dilation_width * (kernel_width - 1) + padding_width + 1

print('height, width is ', height_out, width_out)

