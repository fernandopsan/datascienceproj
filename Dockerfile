#Image with Jupyter notebook and some libraries

FROM python:3.12.13-slim-trixie

RUN mkdir -p /home/projects
WORKDIR /home/projects

RUN pip install numpy \
                pandas \
                matplotlib \
                scikit-learn \
                pyyaml \
                tensorflow \
                seaborn \
                jupyter \
                notebook

EXPOSE 8888
ENTRYPOINT [ "jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser" ]