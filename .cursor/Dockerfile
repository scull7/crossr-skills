# Cloud Agent base image for sycamore-hq/crossr-skills.
# Catalog gates: just, python3, jq. Cargo targets match the current
# CrossR image (rustc 1.83.0). Do not COPY the repo — Cursor checks
# out the requested revision itself.

FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive \
    RUSTUP_HOME=/usr/local/rustup \
    CARGO_HOME=/usr/local/cargo \
    PATH=/usr/local/cargo/bin:/usr/local/bin:${PATH}

USER root
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      build-essential \
      ca-certificates \
      curl \
      git \
      jq \
      python3 \
      sudo \
      unzip \
 && rm -rf /var/lib/apt/lists/* \
 && id -u ubuntu >/dev/null 2>&1 || useradd -m -s /bin/bash ubuntu \
 && echo "ubuntu ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/ubuntu \
 && chmod 0440 /etc/sudoers.d/ubuntu

ARG JUST_VERSION=1.58.0
RUN curl -fsSL "https://github.com/casey/just/releases/download/${JUST_VERSION}/just-${JUST_VERSION}-x86_64-unknown-linux-musl.tar.gz" \
    | tar -xz -C /usr/local/bin just \
 && just --version

ARG RUST_VERSION=1.83.0
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \
    | sh -s -- -y --default-toolchain "${RUST_VERSION}" --profile minimal \
      --component rustfmt,clippy \
 && chmod -R a+rX /usr/local/rustup /usr/local/cargo \
 && rustc --version && cargo --version

USER ubuntu
WORKDIR /home/ubuntu
