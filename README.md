# engineer_example
This repository its about example of data ingestions
# Cria um script temporário no Cloud Shell
cat <<'EOF' > listar_gcp_funcoes.sh
#!/bin/bash

OUTPUT="gcp_services.csv"
echo "project_id,type,name,region,url" > "$OUTPUT"

gcloud projects list --format="value(projectId)" | while read -r PROJECT_ID; do
  echo "📦 Projeto: $PROJECT_ID"

  # Cloud Functions Gen 1
  gcloud functions list --project="$PROJECT_ID" \
    --format="csv[no-heading](name,region,httpsTrigger.url)" 2>/dev/null | \
  while IFS=, read -r NAME REGION URL; do
    echo "$PROJECT_ID,cloud_function_gen1,$NAME,$REGION,$URL" >> "$OUTPUT"
  done

  # Cloud Run (inclui Cloud Functions Gen 2)
  gcloud run services list --platform=managed --project="$PROJECT_ID" \
    --format="json" 2>/dev/null | jq -r --arg pid "$PROJECT_ID" '
      .[] | 
      {
        name: .metadata.name,
        region: .metadata.location,
        url: .status.url,
        managed_by: .metadata.annotations["run.googleapis.com/managed-by"]
      } |
      "\($pid),\((.managed_by == "cloudfunctions")?"cloud_function_gen2":"cloud_run"),\(.name),\(.region),\(.url)"
  ' >> "$OUTPUT"

done

echo "✅ Arquivo gerado: $OUTPUT"
EOF
