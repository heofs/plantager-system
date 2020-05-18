import { gql } from 'apollo-server-express';

export default gql`
  type Query {
    setting(name: String!): Setting!
    lightPlan: LightPlan!
  }

  type Mutation {
    updateLightPlan(value: [UpdateLightPlanInput!]!): LightPlan!
  }

  input UpdateLightPlanInput {
    date: String!
    on: [Int]!
    off: [Int]!
  }

  type LightPlan {
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
