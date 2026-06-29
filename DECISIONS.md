

## 1. In-memory Storage

Used Python lists and dictionaries instead of a database because the assignment explicitly allows in-memory persistence.

---

## 2. Separate Service Layer

Business logic is kept outside the route handlers to improve maintainability and testability.

---

## 3. Single-use Discount Codes

Coupons become invalid after one successful checkout to prevent reuse.

---

## 4. Unlimited Inventory

Inventory validation is intentionally omitted because it is outside the scope of the assignment.

---

## 5. Dataclasses for Domain Models

Used dataclasses for internal models to keep domain objects lightweight while using Pydantic models only for request/response validation.

---

## 6. Order Status Field
Orders are assigned a default status of "confirmed" on creation. 
The field is included to support future status transitions (e.g. pending → confirmed → cancelled).