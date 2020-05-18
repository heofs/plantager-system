import gql from 'graphql-tag';
// import { apolloClient } from 'utils/apollo';

export const GET_LIGHT_CYCLE = gql`
  {
    lightCycle {
      name
      value {
        date
        on
        off
      }
    }
  }
`;

export const UPDATE_LIGHT_CYCLE = gql`
  mutation UpdateLightCycle($lightCycle: [UpdateLightCycleInput!]!) {
    updateLightCycle(value: $lightCycle) {
      name
      value {
        date
        on
        off
      }
    }
  }
`;
