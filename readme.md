name: CI/CD 

on:
  push:
    branches:
      - features
      - releases
  pull_request:
    branches:
      - '*'

jobs:

  init:
    runs-on: ubuntu-latest
    outputs:
      gcloud_project: ${{ steps.setvars.outputs.gcloud_project }}
      phase: ${{ steps.setvars.outputs.phase }}

    steps:
      - name: Cancel previous workflow
        uses: styfle/cancel-workflow-action@0.4.0
        with:
          access_token: ${{ github.token }}

      - name: Set variables
        id: setvars
        run: |
          if [[ "${{github.base_ref}}" == "main" || "${{github.ref}}" == "refs/heads/main" ]]; then
            echo "::set-output name=gcloud_project::main"
            echo "::set-output name=phase::staging"
          fi

          if [[ "${{github.base_ref}}" == "releases" || "${{github.ref}}" == "refs/heads/releases" ]]; then
            echo "::set-output name=gcloud_project::PROD"
            echo "::set-output name=phase::production"
          fi

  Pipeline:
    runs-on: windows-latest
    environment: prod
    needs: init
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2

      - name: Build
        if: startsWith(github.ref, 'refs/heads/features')
        run: |
          # Add your build commands here
          echo "Building..."

      - name: Test
        if: startsWith(github.ref, 'refs/heads/features')
        run: |
          # Add your test commands here
          echo "Testing..."
      
      - name: Acceptance
        if: startsWith(github.ref, 'refs/heads/releases')
        run: |
          # Add your acceptance testing commands here
          echo "Acceptance testing..."
      
      - name: Production
        if: startsWith(github.ref, 'refs/heads/releases')
        run: |
          # Add your production deployment commands here
          echo "Deploying to Production..."

      - name: Get Branch Name
        run: |
          
          echo "${{ vars.DB_HOST }}"


 