import h5py
import json
import shutil

# Copy original model first
shutil.copy("app/ml_model/model.h5", "app/ml_model/model_fixed.h5")

with h5py.File("app/ml_model/model_fixed.h5", "r+") as f:
    config = json.loads(f.attrs["model_config"])

    def fix(obj):
        if isinstance(obj, dict):
            if obj.get("class_name") == "BatchNormalization":
                cfg = obj["config"]
                cfg.pop("renorm", None)
                cfg.pop("renorm_clipping", None)
                cfg.pop("renorm_momentum", None)

            for value in obj.values():
                fix(value)

        elif isinstance(obj, list):
            for item in obj:
                fix(item)

    fix(config)

    f.attrs.modify("model_config", json.dumps(config))

print("Model repaired successfully!")