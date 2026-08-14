FROM haskell:9.4-slim
WORKDIR /app
COPY haskell/ /app/haskell/
WORKDIR /app/haskell
RUN cabal update && cabal build all
ENTRYPOINT ["sh", "-c", "for s in section1_correction_b section2_preprint section3_ab_cloud section4_kdv section5_klein_attractor section6_riemann_zeros; do cabal run verify_$s; done"]
