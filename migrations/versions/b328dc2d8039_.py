"""empty message

Revision ID: b328dc2d8039
Revises: 
Create Date: 2024-05-08 02:57:57.323365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b328dc2d8039'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('vehicle_id', sa.Integer(), nullable=True),
    sa.Column('route_id', sa.Integer(), nullable=True),
    sa.Column('subroute_id', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('transaction_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['route_id'], ['routes.id'], ),
    sa.ForeignKeyConstraint(['subroute_id'], ['subroutes.id'], ),
    sa.ForeignKeyConstraint(['transaction_id'], ['transactions.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('business',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('contact', sa.String(length=50), nullable=True),
    sa.Column('currency', sa.String(length=10), nullable=True),
    sa.Column('country', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('routes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_location', sa.String(length=100), nullable=True),
    sa.Column('stop_location', sa.String(length=100), nullable=True),
    sa.Column('duration', sa.String(length=50), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('payment_id', sa.Integer(), nullable=True),
    sa.Column('phone_number', sa.Integer(), nullable=True),
    sa.Column('booking_id', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('status', sa.Enum('pending', 'successful', 'failed'), nullable=True),
    sa.Column('reference_code', sa.String(length=15), nullable=True),
    sa.Column('vehicle_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['booking_id'], ['bookings.id'], ),
    sa.ForeignKeyConstraint(['payment_id'], ['payments.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vehicle_number', sa.String(length=20), nullable=True),
    sa.Column('vehicle_type', sa.String(length=50), nullable=True),
    sa.Column('current_location', sa.String(length=100), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.Column('transaction_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['transaction_id'], ['transactions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payout_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('preferred_option', sa.Enum('MPESA', 'bank'), nullable=True),
    sa.Column('mpesa_reference', sa.Enum('Paybill', 'Till Number'), nullable=True),
    sa.Column('bank_code', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bank_code'], ['business.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subroutes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_location', sa.String(length=100), nullable=True),
    sa.Column('stop_location', sa.String(length=100), nullable=True),
    sa.Column('duration', sa.String(length=50), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('route_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['route_id'], ['routes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('role', sa.Enum('passenger', 'business manager', 'Intasend admin'), nullable=True),
    sa.Column('phone_number', sa.String(length=20), nullable=True),
    sa.Column('business_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['business_id'], ['business.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('reference_code', sa.String(length=15), nullable=True),
    sa.Column('payment_method', sa.Enum('MPESA', 'Bank'), nullable=True),
    sa.Column('transaction_id', sa.Integer(), nullable=True),
    sa.Column('internal_reference', sa.String(length=15), nullable=True),
    sa.Column('timestamp', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payments')
    op.drop_table('users')
    op.drop_table('subroutes')
    op.drop_table('payout_details')
    op.drop_table('vehicles')
    op.drop_table('transactions')
    op.drop_table('routes')
    op.drop_table('business')
    op.drop_table('bookings')
    # ### end Alembic commands ###