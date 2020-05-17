import gql from 'graphql-tag';
import { apolloClient } from 'utils/apollo';

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
