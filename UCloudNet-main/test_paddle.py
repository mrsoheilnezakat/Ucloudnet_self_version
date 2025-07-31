import paddle

# Print version
print("Paddle version:", paddle.__version__)

# Check if compiled with CUDA
print("Compiled with CUDA:", paddle.is_compiled_with_cuda())

# Check if GPU is available
print("CUDA available:", paddle.device.is_compiled_with_cuda())
print("GPU device:", paddle.get_device())
