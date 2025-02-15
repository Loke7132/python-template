# Component Specification

## Calculator
- **Type**: Arithmetic Processor
- **Methods**:
  - `add(a: float, b: float) -> float`
  - `subtract(a: float, b: float) -> float`
  - `multiply(a: float, b: float) -> float`

## Logger
- **Type**: Audit Trail
- **Methods**:
  - `log_operation(operation: str, result: float)`

## Notifier
- **Type**: Threshold Monitor
- **Methods**:
  - `check_threshold(value: float) -> bool`
