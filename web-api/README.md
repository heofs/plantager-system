```graphql
mutation {
  lightCycle(
    value: [
      { date: "start", on: [6, 0], off: [21, 0] }
      { date: "25-07-20", on: [9, 0], off: [21, 0] }
    ]
  ) {
    name
    value {
      date
      on
      off
    }
  }
}
```