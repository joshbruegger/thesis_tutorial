from ultralytics import YOLO

model = YOLO('yolov8m.pt')

results = model.train(
    data='dataset.yaml',
    epochs=10,
    batch=-1,
    name='svhn',
)
