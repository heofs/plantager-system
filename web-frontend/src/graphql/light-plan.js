import gql from 'graphql-tag';
// import { apolloClient } from 'utils/apollo';

export const GET_LIGHT_PLAN = gql`
  {
    lightPlan {
      name
      value {
        date
        on
        off
      }
    }
  }
`;

export const UPDATE_LIGHT_PLAN = gql`
  mutation UpdateLightPlan($lightPlan: [UpdateLightPlanInput!]!) {
    updateLightPlan(value: $lightPlan) {
      name
      value {
        date
        on
        off
      }
    }
  }
`;
