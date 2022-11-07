# GKE cluster
resource "google_container_cluster" "primary" {
  name     = "${var.project_id}-gke"
  location = var.region
  network    = google_compute_network.vpc.name
  subnetwork = google_compute_subnetwork.subnet.name
  initial_node_count = "1"
  node_config {
    labels = {
      app = "flight-dev"
    }
  }
}