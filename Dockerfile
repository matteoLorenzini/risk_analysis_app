# syntax=docker/dockerfile:1
# Base image: using the public ResearchSpace image. Adjust tag if you need a specific version.
FROM ghcr.io/researchspace/researchspace:latest

# --- Assumptions -----------------------------------------------------------
# The runtime data (templates, config, ldp) is normally mounted as a volume.
# For a baked image we COPY them inside. Path may differ by version; if your
# container expects /opt/researchspace/runtime-data or /app/runtime-data adjust below.
# Here we assume /app/runtime-data as a writable location used in many setups.
# ---------------------------------------------------------------------------

# Create target runtime-data directory (if not already present in base image)
RUN mkdir -p /app/runtime-data/config \
    && mkdir -p /app/runtime-data/data/templates \
    && mkdir -p /app/runtime-data/ldp

# Copy configuration and data. These will override what's in the base image at build time.
# If some folders are absent, build will still succeed.
COPY config/ /app/runtime-data/config/
COPY data/ /app/runtime-data/data/
COPY ldp/ /app/runtime-data/ldp/

# Optional: set environment variables (uncomment & adjust if needed)
# ENV JAVA_OPTS="-Xms256m -Xmx1g"

# Healthcheck (optional) - adjust URL/port if different
# HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD curl -f http://localhost:10214/ || exit 1

# The base image should already define the entrypoint / startup; no CMD needed.
# You can uncomment below if you need a custom startup script.
# CMD ["/docker-entrypoint.sh"]

# Notes:
# - After pushing this image, update your docker compose service definition to:
#     image: ghcr.io/<owner>/risk_analysis_app:latest
#   or keep using build: . with compose building from this Dockerfile.
# - Ensure compose does not also mount the same runtime-data folders unless you
#   want to override what is baked into the image.
