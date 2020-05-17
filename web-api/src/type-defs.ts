import { gql } from 'apollo-server-express';

export default gql`
  type Query {
    setting(name: String!): Setting!
    lightCycle: LightCycle!
  }

  type Mutation {
    lightCycle(value: [UpdateLightCycleInput!]!): LightCycle!
  }

  input UpdateLightCycleInput {
    date: String!
    on: [Int]!
    off: [Int]!
  }

  type LightCycle {
    name: String!
    value: [Cycle]!
  }

  type Cycle {
    date: String!
    on: [Int]!
    off: [Int]!
  }

  type Setting {
    name: String!
    value: String
  }
`;
