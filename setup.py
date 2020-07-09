from setuptools import setup


setup(
    name="nb-tfjs_mnist",
    packages= ['tfjs_mnist'],
    version='0.0.1',
    include_package_data=True,
    install_requires=[
        'jupyter-server-proxy',
        'notebook'
    ],
    url="https://github.com/ouseful-PR/Hand-Written-Digit-Recognition",
    author="",
    description="tony.hirst@gmail.com",
    entry_points={
        'jupyter_serverproxy_servers': [
            'tfjs_mnist = tfjs_mnist:setup_tfjs_mnist',
        ]
    })