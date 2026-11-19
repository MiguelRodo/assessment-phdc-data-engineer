# Competency assessment for data scientist position at CIDER

This repository contains the executable solution for the PHDC data engineer challenge.

## Contact

For more information, please contact:

- Miguel J. Rodo: miguel.rodo@uct.ac.za

## Execution

To execute the pipeline, run:

```sh

```

## Links

- [Instructions repo](https://github.com/wc-phdc-hia/data-competency-assessment)
- [Data portal](https://odp-cctegis.opendata.arcgis.com/datasets/cctegis::service-requests-2023-until-06-october-2026-deprecated/explore)

## Details

### Method of finding endpoint

1. Navigate to provided URL.
2. Click `Info`.
3. Click `View API Resources`.
4. Copy `GeoService` field.

### Dataset's schema

At https://services6.arcgis.com/nyYfO9SxHU2ChQd9/arcgis/rest/services/Service_Requests_2023_until_20_May_2026/FeatureServer/0, the `Fields` key lists the following components:

- Sub_Council, Ward, Surb, C3_Complaint_Type, Work_Center, Notification, Notification_type, X_Y_Co_ordinate_1, X_Y_coordinate_2, Created_On_Date, Changed_on, Completed_Date, Notifications_Created and ObjectId, which have string, integer, date or objectid types.

### Issues with suburb column

- Street addresses
- Uninformative addresses