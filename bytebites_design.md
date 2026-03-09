+------------------------+                    +------------------------+
|      Customer          |                    |       Menu             |
+------------------------+                    +------------------------+
| - name: str            |                    | - items: list<Item>    |
| - purchase_history: [] |                    +------------------------+
+------------------------+                    | + add_item(item): void |
| + add_order(): void    |                    | + filter_by_category() |
| + verify_user(): bool  |                    +------------------------+
+------------------------+                              |
        |                                                |
        | creates                                        | contains
        |                                                |
        v                                                v
+------------------------+                    +------------------------+
|       Order            |1..*                |      FoodItem          |
+------------------------+------>             +------------------------+
| - items: list<Item>    |                    | - name: str            |
+------------------------+                    | - price: float         |
| + add_item(): void     |                    | - category: str        |
| + compute_total(): fl  |                    | - popularity_rating: fl|
+------------------------+                    +------------------------+