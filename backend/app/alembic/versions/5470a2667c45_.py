"""empty message

Revision ID: 5470a2667c45
Revises: 
Create Date: 2022-04-30 11:04:27.432573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5470a2667c45'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flights',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('departureDate', sa.DateTime(), nullable=True),
    sa.Column('departureAirportCode', sa.String(length=60), nullable=True),
    sa.Column('departureAirportName', sa.String(length=100), nullable=True),
    sa.Column('departureCity', sa.String(length=255), nullable=True),
    sa.Column('departureLocale', sa.String(length=255), nullable=True),
    sa.Column('arrivalDate', sa.DateTime(), nullable=True),
    sa.Column('arrivalAirportCode', sa.String(length=60), nullable=True),
    sa.Column('arrivalAirportName', sa.String(length=100), nullable=True),
    sa.Column('arrivalCity', sa.String(length=255), nullable=True),
    sa.Column('arrivalLocale', sa.String(length=255), nullable=True),
    sa.Column('ticketPrice', sa.Integer(), nullable=True),
    sa.Column('ticketCurrency', sa.String(length=60), nullable=True),
    sa.Column('flightNumber', sa.Integer(), nullable=True),
    sa.Column('seatCapacity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('fullname', sa.String(length=255), nullable=True),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('status', sa.String(length=40), nullable=True),
    sa.Column('outboundFlight_id', sa.Integer(), nullable=True),
    sa.Column('paymentToken', sa.String(length=100), nullable=True),
    sa.Column('checkedIn', sa.Boolean(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('createdAt', sa.DateTime(), nullable=True),
    sa.Column('bookingReference', sa.String(length=40), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['users.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['outboundFlight_id'], ['flights.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('bookingReference')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookings')
    op.drop_table('users')
    op.drop_table('flights')
    # ### end Alembic commands ###
